from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def save_to(instance, filename):
    profile_username = instance.user.username
    return f'profiles/{profile_username}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), on_delete=models.CASCADE)
    first_name = models.CharField(verbose_name=_('Name'), max_length=100, blank=True)
    last_name = models.CharField(verbose_name=_('Surname'), max_length=100, blank=True)
    about = models.TextField(verbose_name=_('About'), max_length=500, blank=True)
    photo = models.FileField(verbose_name=_('Profile photo'), blank=True, upload_to=save_to)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
