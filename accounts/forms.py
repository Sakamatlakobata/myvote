from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django.forms               import ModelForm
from django                     import forms
from .models                    import Accounts


class UserForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2',] # limit the fields

class AccountsForm(forms.ModelForm):
    class Meta:
        model  = Accounts
        fields = ['zipcode',] # limit the fields
