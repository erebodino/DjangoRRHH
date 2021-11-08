from django import forms

class LoginForm (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))


