from django.forms import ModelForm
# from .models import 
from django import forms
from .models import User

class RegisterForm(ModelForm):
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'firstName', 'lastName', 'password', 'userLevel']

# class RegisterForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"1"}))
#     password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"1"}))
#     firstName = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     lastName = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"1"}))
#     userLevelList = (
#         ('1','Faculty'),
#         ('2','Department Head'),
#         ('3','Research Coordinator'),
#         ('4','Extension Coordinator'),
#     )
#     userLevel = forms.ChoiceField(label="Role", choices=userLevelList, widget=forms.Select(attrs={"class":"1"}))
#     class Meta:
#         model = User