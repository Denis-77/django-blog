from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from registration.models import Profile


class RegistrationForm(UserCreationForm):
    #  USER
    email = forms.EmailField(max_length=254, label='Email', required=True)
    #  PROFILE
    first_name = forms.CharField(max_length=100, label=_('Name'), required=False)
    last_name = forms.CharField(max_length=100, label=_('Surname'), required=False)
    about = forms.CharField(max_length=500, label=_('About'), required=False, widget=forms.Textarea)
    photo = forms.FileField(label=_('Photo'), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'about', 'photo')
