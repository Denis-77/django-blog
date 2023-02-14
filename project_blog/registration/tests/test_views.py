from django.test import TestCase
from django.contrib.auth.models import User
from registration.models import Profile


class ViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='TestUser',
            email='test@mail.com',
            password='1111'
        )
        Profile.objects.create(
            user=user
        )

    def test_my_profile_view(self):
        self.client.login(username='TestUser', password='1111')
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/profile.html')

    def test_registration_view(self):
        response = self.client.get('/accounts/registration/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')

    def test_login_view(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
