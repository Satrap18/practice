from django import forms

class LoginForms(forms.Form):

    username = forms.CharField(widget=forms.TextInput, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True) 