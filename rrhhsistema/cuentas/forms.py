from django import forms

class LoginForm (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm'}))


class OrdenarForm (forms.Form):
    fecha_inicio = forms.DateField(widget=forms.SelectDateWidget)
    fecha_fin = forms.DateField(widget=forms.SelectDateWidget)
    archivo = forms.FileField(widget=forms.FileInput)


