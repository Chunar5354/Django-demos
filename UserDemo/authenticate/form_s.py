from django import forms


class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

class UserRegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField()

