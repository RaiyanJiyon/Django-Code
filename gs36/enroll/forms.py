from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField(label="Phone Number")
    password = forms.CharField(widget=forms.PasswordInput)