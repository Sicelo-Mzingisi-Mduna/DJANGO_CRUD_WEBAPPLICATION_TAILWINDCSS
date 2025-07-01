from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm 
from django.forms.widgets import TextInput, Textarea, EmailInput, PasswordInput
from typing import Any, Dict

from .models import Customer

# - Register / Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
       
# - Login a user

class LoginForm(AuthenticationForm):
  username = forms.CharField(widget = TextInput())
  password = forms.CharField(widget = PasswordInput())
  
# - Create a customer form
from django import forms
from django.forms import TextInput, Textarea, EmailInput
from .models import Customer  # Make sure Customer is imported

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['FirstName', 'LastName', 'Email', 'Phone', 'Address', 'City', 'Province', 'Country', 'Zipcode']
        labels = {
            'FirstName': 'FirstName',
            'LastName': 'LastName',
            'Email': 'Email',
            'Phone': 'Phone',
            'Address': 'Address',
            'City': 'City',
            'Province': 'Province',
            'Country': 'Country',
            'Zipcode': 'Zipcode',
        }
        widgets = {
            'FirstName': TextInput(attrs={'placeholder': 'Enter first name'}),
            'LastName': TextInput(attrs={'placeholder': 'Enter last name'}),
            'Email': EmailInput(attrs={'placeholder': 'Enter email'}),
            'Phone': TextInput(attrs={'placeholder': 'Enter phone number'}),
            'Address': Textarea(attrs={'placeholder': 'Enter address', 'rows': 3}),
            'City': TextInput(attrs={'placeholder': 'Enter city'}),
            'Province': TextInput(attrs={'placeholder': 'Enter province'}),
            'Country': TextInput(attrs={'placeholder': 'Enter country'}),
            'Zipcode': TextInput(attrs={'placeholder': 'Enter zipcode'}),
        }
        

  