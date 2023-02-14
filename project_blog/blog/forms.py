from django import forms
from django.utils.translation import gettext_lazy as _


class CreateEntryForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label=_('Title'))
    content = forms.CharField(max_length=500, required=True, label=_('Content'), widget=forms.Textarea)
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                            label=_('Add photo'),
                            required=False)


class CSVEntryForm(forms.Form):
    file = forms.FileField(label=_('File'))
