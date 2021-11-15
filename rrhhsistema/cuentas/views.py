from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, OrdenarForm

def base(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'base.html')
        else:    
            form = LoginForm()
            form_orden = OrdenarForm()
            return render(request, 'cuentas/login.html', {'form': form,
            'form_orden':form_orden})
    else:
        valor = user_login(request)
        return valor


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        print(request.POST)
        print('')

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['usuario'],
                                password=cd['contraseña'])
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        form_orden = OrdenarForm()
    return render(request, 'cuentas/login.html', {'form': form,
    'form_orden':form_orden})
# Create your views here.
