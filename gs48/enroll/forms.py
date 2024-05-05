from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
    
    # Here, we can't use labels, help_text, widgets etc in this method. 