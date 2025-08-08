from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError




class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
    conf_password = forms.CharField(label='confrim password',widget=forms.PasswordInput(attrs={'placeholder':'Confrim Password','class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists!')
        return email
    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('This username already exists!')
        return username
    def clean(self):
        cd = super().clean()
        p = cd.get('password')
        cp = cd.get('conf_password')

        if p and cp and p != cp:
            raise ValidationError('password is not match!')

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username or Email',widget=forms.TextInput(attrs={'placeholder':'Username or Email','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'form-control'}))
