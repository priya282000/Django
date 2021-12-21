from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.core.validators import RegexValidator
from .models import user_reg, book_details


class RegistrationForm(forms.Form):


    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    user_name = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    repassword = forms.CharField(label='Retype password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')

    def clean(self):
        cleaned_data = super().clean()
        pwd = self.cleaned_data.get('password')
        rpwd = self.cleaned_data.get('repassword')
        if pwd != rpwd:
            raise forms.ValidationError('Password mismatched!')
        return pwd


    class Meta:
        model = user_reg
        fields = {'first_name', 'last_name', 'user_name', 'password', 'email'}


class BookDetails(forms.Form):
    class Meta:
        model = book_details
        fields = '__all__'
