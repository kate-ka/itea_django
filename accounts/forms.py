from django import forms
from .models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'mobile_number',
                  'home_address',
                  'photo',
                  'gender']
