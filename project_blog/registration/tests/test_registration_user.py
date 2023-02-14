from django.test import TestCase
from django.contrib.auth.models import User

from registration.models import Profile


class ViewsTests(TestCase):

    def test_create_and_update_profile(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 403) # as anonymous user
        self.client.post('/accounts/registration/', { # create profile
            'username': 'TestUser',
            'email': 'aa@a.ds',
            'password1': 'pass11WORD#',
            'password2': 'pass11WORD#',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'about': 'about'
        })
        user = User.objects.get(id=1) # get created user from db
        self.assertEqual(user.username, 'TestUser')
        self.assertEqual(user.profile.first_name, 'first_name')
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200) # as authenticated user
        # UPDATE PROFILE
        self.client.post('/accounts/profile/', {
            'first_name': 'another_first_name',
            'last_name': 'another_last_name',
            'about': 'another_about'
        })
        profile = Profile.objects.get(id=1)
        self.assertEqual(
            (profile.first_name, profile.last_name, profile.about),
            ('another_first_name', 'another_last_name', 'another_about')
        )