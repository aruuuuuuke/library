# from django.db import models
# from django.contrib.auth.models import User
#
#
# class CustomUser(User):
#     Gender = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     phone_number = models.CharField(max_length=15 )
#     age = models.PositiveIntegerField()
#     gender = models.CharField(max_length=1, choices=Gender)
#     club = models.CharField(max_length=100)
#
#
#     def save(self, *args, **kwargs):
#         if self.age < 7:
#             self.age = "Еще не дарос"
#         elif 7 <= self.age < 12:
#             self.club = "Детский"
#         elif 12 <= self.age < 18:
#             self.club = "Подростковый"
#         elif 18 <= self.age < 60:
#             self.club = "Взрослый"
#         else:
#             self.club = "Пора отдохнуть"
#
#     super().save()
