from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.utils.datastructures import MultiValueDictKeyError

from registration.forms import RegistrationForm, EditProfileForm
from registration.models import Profile


def my_profile_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    if request.method == 'POST':
        profile = request.user.profile
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            try:
                profile.photo = request.FILES['photo']
            except MultiValueDictKeyError:
                print('Без фото')
            profile.save()
            return redirect('/')
    else:
        profile = request.user.profile
        form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, 'registration/profile.html', context=context)


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            about = form.cleaned_data.get('about')
            photo = form.cleaned_data.get('photo')
            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                about=about,
                photo=photo,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/registration.html', context=context)


class MyLoginView(LoginView):
    template_name = 'registration/login.html'


def logout_view(request):
    logout(request)
    return redirect('/')
