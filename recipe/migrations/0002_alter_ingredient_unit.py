# Generated by Django 5.1.5 on 2025-01-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('граммы', 'гр'), ('килограммы', 'кг'), ('миллилитры', 'мл'), ('литры', 'л'), ('штуки', 'шт')], max_length=10, null=True),
        ),
    ]
