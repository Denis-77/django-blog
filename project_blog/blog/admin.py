from django.contrib import admin
from blog.models import Entry, Photo
from django.utils.translation import gettext_lazy as _


class PhotoInline(admin.TabularInline):
    model = Photo


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_content', 'creation_date')
    inlines = [PhotoInline]

    @admin.display(description=_('Short content'))
    def short_content(self, obj):
        content = obj.content
        if len(content) > 100:
            content = ' '.join([content[:100], '...'])
        return content
