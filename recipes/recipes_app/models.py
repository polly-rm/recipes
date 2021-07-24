from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
    )
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=250,
    )

    def split_ingredients(self):
        return self.ingredients.split(', ')

    time = models.IntegerField()
