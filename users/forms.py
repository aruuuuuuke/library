from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Введите Email')
    phone_number = forms.CharField(required=True, label='Введите номер телефона')
    age = forms.IntegerField(required=True, label='Укажите возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone_number',
        )

    def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.phone_number = self.cleaned_data['phone_number']
            user.age = self.cleaned_data['age']
            user.gender = self.cleaned_data['gender']

            if commit:
                user.save()
            return user

