from django.urls import path, include
from blog.views import show_all, detail_view, create_view, csv_entries


urlpatterns = [
    path('', show_all, name='main'),
    path('entries/<int:entry_id>/', detail_view, name='detail'),
    path('entries/create/', create_view, name='create_entry'),
    path('entries/multiadd/', csv_entries, name='multiadd'),
    path('i18n', include('django.conf.urls.i18n')),
]
