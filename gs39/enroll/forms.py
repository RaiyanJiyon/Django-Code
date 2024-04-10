from django import forms 

class StudentRegistration(forms.Form):
    firstname = forms.CharField(min_length=5, error_messages={'required': 'Enter your First Name with minimum 5 characters'})
    lastname = forms.CharField(max_length=10, strip=False)
    nickname = forms.CharField(empty_value='Sam')
    roll = forms.IntegerField(min_value=5, max_value=10)
    fees = forms.DecimalField(min_value=5, max_value=40, max_digits=4, decimal_places=1)
    CGPA = forms.FloatField(min_value=1, max_value=4)
    comment = forms.SlugField()
    email = forms.EmailField(min_length=10, max_length=100)
    website = forms.URLField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=5, max_length=20)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':20}))
    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'somecss1', 'id': 'uniqueid1'}))
    notes = forms.CharField(min_length=5, max_length=50, widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    agree = forms.BooleanField(label_suffix='', label='I Agree', error_messages={'required': 'Please check the agree button.'})
