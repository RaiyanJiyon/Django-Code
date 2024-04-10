from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_name(self):
        data = self.cleaned_data["name"]
        
        if len(data) < 4:
            raise forms.ValidationError('Enter more than or equal 4 character.')
            
        return data
    