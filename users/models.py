from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, blank=True)
    experience = models.PositiveIntegerField(default=7, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    salary = models.CharField(max_length=100,blank=True)
    specialization = models.CharField(max_length= 50, blank=True)


    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.salary = "Вам надо еще набраться опыта"
        elif 1 <= self.experience  < 3:
            self.salary = 'Ваша зарплата будет 1000$'
        elif 3 <= self.experience  < 6:
            self.salary = 'Ваша зарплата будет 2000$'
        elif 6 <= self.experience  <= 10:
            self.salary = 'Ваша зарплата будет 5000$'
        else:
            self.salary = "Пора отдохнуть"

        super().save(*args, **kwargs)