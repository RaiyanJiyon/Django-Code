from typing import Any
from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        valname = self.cleaned_data['name']
        if len(valname) <= 4:
            raise forms.ValidationError('Enter more than 4 character')
        

        valemail = self.cleaned_data['email']
        if len(valemail) < 10:
            raise forms.ValidationError('Enter email address more than 10 character')
        

        valpassword = self.cleaned_data['password']
        if len(valpassword) < 8:
            raise forms.ValidationError('Enter password more than 8 character')
        