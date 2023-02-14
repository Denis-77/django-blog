from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Entry(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    content = models.TextField(max_length=500, verbose_name=_('Content'))
    creation_date = models.DateField(verbose_name=_('Creation date'), auto_now_add=True, db_index=True)
    author = models.ForeignKey(User, verbose_name=_('Author'), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        permissions = (
            ('multiadd', 'загрузка нескольких записей'),
        )


def save_to(instance, filename):
    entry_id = instance.entry.id
    return f'blog/{entry_id}/{filename}'


class Photo(models.Model):
    file = models.FileField(upload_to=save_to, verbose_name=_('File'))
    entry = models.ForeignKey(Entry, verbose_name=_('Entry'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
