from django import forms
from .models import user_reg, book_details
import re


class RegistrationForm(forms.ModelForm):
    """ Registration form details """
    first_name = forms.CharField(label='First name')
    last_name = forms.CharField(label='Last name')
    user_name = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    repassword = forms.CharField(label='Retype password', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email')

    field_order = ['first_name', 'last_name', 'user_name', 'password', 'repassword', 'email']

    def clean(self):
        """ Check if password and retype password are same """
        cleaned_data = super().clean()
        pwd = self.cleaned_data['password']
        rpwd = self.cleaned_data['repassword']
        reg = "^(?=.*[a-z])" \
              "(?=.*[A-Z])" \
              "(?=.*\d)" \
              "(?=.*[@$!%*#?&])" \
              "[A-Za-z\d@$!#%*?&]" \
              "{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, pwd)
        if pwd != rpwd:
            raise forms.ValidationError("Password Mismatched")
        elif not mat:
            raise forms.ValidationError(
                "Password should have at least one number. "
                "\nShould have at least one uppercase and one lowercase character. "
                "\nShould have at least one special symbol."
                "\nShould be between 6 to 20 characters long."
            )

        return cleaned_data

    class Meta:
        """ insert form details into user_reg model """
        model = user_reg
        fields = {'first_name', 'last_name', 'user_name', 'password', 'email'}


class BookDetails(forms.ModelForm):
    """ Book details form """

    class Meta:
        """ Save book details into book_details model """
        model = book_details
        fields = '__all__'


class LoginForm(forms.Form):
    """ Login form """
    user_name = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    ordered_field_names = {'user_name', 'password'}
