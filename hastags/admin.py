from django.contrib import admin
from . import models

admin.site.register(models.Tag)
admin.site.register(models.Genre)

# Register your models here.
