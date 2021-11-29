from django import forms
from .models import AreaModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import Profile





class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('dni','area', 'legajo', 'fecha_ingreso')


class LoginForm (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))


class OrdenarForm (forms.Form):
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    archivo = forms.FileField(widget=forms.FileInput)
    fecha_feriado = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))


