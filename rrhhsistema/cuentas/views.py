from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, OrdenarForm, ProfileForm, UserRegistrationForm 
from .models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def base(request):
    return render(request, 'base.html')



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

def creacion_usuario(request):

       if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile


            #Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
        else:
            user_form = UserRegistrationForm()
        return render(request,
                    'account/register.html',
                    {'user_form': user_form})

def register(request):
    if request.method == 'POST':
        print('='*30)
        print(request.POST)
        print('='*30)
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            print(user_form.cleaned_data)
            print("")
            print("=========================")
            print(profile_form.cleaned_data)
            print("")
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            return render(request,
                          'cuentas/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()
    return render(request,
                  'cuentas/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})


