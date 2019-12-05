from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Recipe, Ingredient, Step
from .serializers import UserSerializer, RecipeSerializer, IngredientSerializer, StepSerializer

# Create your views here.
class AllRecipes(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class UserRecipes(APIView):
    def get_object(self, user_id):
        try:
            return Recipe.objects.get(user_id=user_id)
        except:
            return status.HTTP_404_NOT_FOUND

    def get(self, request, user_id, format=None):
        recipes = Recipe.objects.filter(user_id=user_id)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, user_id):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        recipe = self.get_object(user_id)
        print('\nDeleting Recipe', user_id, '\n')
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, user_id):
        print("Recipe Put Call")
        recipe = self.get_object(user_id)
        print("Getting Object")
        serializer = RecipeSerializer(recipe, data=request.data)  
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

