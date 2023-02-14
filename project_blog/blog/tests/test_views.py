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

    def test_show_all_view(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_create_view(self):
        response = self.client.get('/entries/create/')
        self.assertEqual(response.status_code, 403) # as anonymous user
        self.client.login(username='TestUser', password='1111')
        response = self.client.get('/entries/create/')
        self.assertEqual(response.status_code, 200) # as authenticated user
        self.assertTemplateUsed(response, 'blog/create_entry.html')

    def test_csv_entries_view(self):
        response = self.client.get('/entries/multiadd/')
        self.assertEqual(response.status_code, 403) # as anonymous user
        self.client.login(username='TestUser', password='1111')
        response = self.client.get('/entries/multiadd/')
        self.assertEqual(response.status_code, 200) # as authenticated user
        self.assertTemplateUsed(response, 'blog/csv_multiadd.html')