from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'




class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('граммы', 'гр'),
        ('килограммы','кг'),
        ('миллилитры', 'мл'),
        ('литры', "л"),
        ('штуки', "шт"),
    ]
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.quantity} {self.unit}'
