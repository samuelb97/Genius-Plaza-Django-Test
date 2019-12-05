from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('recipes', views.AllRecipes.as_view()),
    path('recipes/<int:user_id>', views.UserRecipes.as_view())
]