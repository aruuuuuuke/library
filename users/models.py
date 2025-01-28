from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14)
    experience = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER)
    salary = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.salary = "У вас недостаточно опыта"
        elif 1 <= self.experience < 3:
            self.salary = '1000$'
        elif 3 <= self.experience < 6:
            self.salary = '2000$'
        elif 6 <= self.experience <= 10:
            self.salary = '5000$'
        else:
            self.salary = "Может быть пора отдохнуть"

        super().save(*args, **kwargs)
