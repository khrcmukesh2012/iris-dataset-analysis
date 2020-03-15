from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
class UserForm(ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))



	class Meta:
	    model = User
	    fields = ('username', 'email', 'password')