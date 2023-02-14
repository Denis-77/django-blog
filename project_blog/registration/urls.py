from django.urls import path
from registration.views import my_profile_view, registration_view, logout_view, MyLoginView


urlpatterns = [
    path('profile/', my_profile_view, name='profile'),
    path('registration/', registration_view, name='registration'),
    path('logout/', logout_view, name='logout'),
    path('login/', MyLoginView.as_view(), name='login'),
]
