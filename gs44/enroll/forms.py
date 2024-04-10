from typing import Any
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='Re-Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        valpwd = cleaned_data['password']
        valrepwd = cleaned_data['repassword']

        if valpwd != valrepwd:
            raise forms.ValidationError('Password does not match')