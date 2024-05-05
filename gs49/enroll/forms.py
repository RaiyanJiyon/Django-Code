from django import forms
from .models import User

# Solving ModelForm in Django-1 problems in here 

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {'name': 'Full Name:', 'email': 'Enter Email:', 'password': 'Enter Password:'}
        error_messages = {
            'name': {'required': 'You have to must enter your name'},
            'password': {'required': 'You have to must enter your password'}
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter your name here'})
        }