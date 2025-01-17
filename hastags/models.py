from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(verbose_name="Укажите цену", default=300, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name