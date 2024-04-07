from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(label='Full Name', label_suffix=' ', initial='Enter Your Name', disabled=True, help_text='Max Character should be 70')