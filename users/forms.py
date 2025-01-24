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
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')
    experience = forms.IntegerField(required=True, label='Укажите свой опыт  работы')
    specialization = forms.CharField(required=True,  label='Укажите ваше направление')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'specialization',
            'first_name',
            'last_name',
            'experience',
            'gender',
            'phone_number',
        )

    def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            user.specialization = self.cleaned_data['specialization']
            user.phone_number = self.cleaned_data['phone_number']
            user.experience = self.cleaned_data['experience']
            user.gender = self.cleaned_data['gender']

            if commit:
                user.save()
            return user