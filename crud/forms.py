from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
# from django.forms.widgets import TextInput,PasswordInput
from .models import Record



#  Create User Form

class CreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    # Remove help Text
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text =None
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None



#  Login User Form

class LoginForm(AuthenticationForm):
    username =forms.CharField(widget=forms.TextInput)
    password =forms.CharField(widget=forms.PasswordInput)


# Create a record 

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']


# Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']

