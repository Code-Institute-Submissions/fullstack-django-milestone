from django import forms

class PlainUserForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email =  forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
