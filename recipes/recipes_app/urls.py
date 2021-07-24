from django.urls import path

from recipes.recipes_app.views import create_recipe, edit_recipe, delete_recipe, show_recipe_details, index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', show_recipe_details, name='recipe details'),
]