from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User, Ingredient, Recipe, Step

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'firstname', 'lastname')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'text')

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('id', 'step_text')

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id','name', 'user', 'ingredients', 'steps')

    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        steps= validated_data.pop('steps')
        print('Create Ingredients: ', ingredients)
        print('Create Steps: ', steps)

        recipe = Recipe.objects.create(**validated_data)

        for ingredient in ingredients:
            Ingredient.objects.create(recipe=recipe, **ingredient)

        for step in steps:
            Step.objects.create(recipe=recipe, **step)

        return recipe

    def update(self, instance, validated_data):
        new_ingredients = validated_data.pop('ingredients')
        new_steps = validated_data.pop('steps')

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        instance.ingredients.all().delete()
        for ingredient in new_ingredients:
            print('\n Update Ingredient: ', ingredient.get('text'), '\n')
            Ingredient.objects.create(recipe=instance, **ingredient)

        instance.steps.all().delete()
        for step in new_steps:
            print('\n Update Step: ', step, '\n')
            Step.objects.create(recipe=instance, **step)

        return instance

