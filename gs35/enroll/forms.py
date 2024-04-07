from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    gender = forms.CharField(widget=forms.HiddenInput())
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'somecss1', 'id': 'uniqueid'}))
    age = forms.CharField(widget=forms.CheckboxInput())
    photos = forms.CharField(widget=forms.FileInput())