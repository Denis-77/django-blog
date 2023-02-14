from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Entry


NUMBER_OF_ENTRIES = 10


class TestEntries(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='TestUser',
            email='test@mail.com',
            password='1111'
        )
        for entry_index in range(NUMBER_OF_ENTRIES):
            Entry.objects.create(
                title=f'TestEntry{entry_index}',
                content='FishText',
                author = user
            )

    def test_entries_number(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['entries']) == NUMBER_OF_ENTRIES)

    def test_detail_view(self):
        response = self.client.get('/entries/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/entry_item.html')

    def test_create_entries(self):
        self.client.login(username='TestUser', password='1111')
        self.client.post('/entries/create/', {
            'title': 'TestEntryNew',
            'content': 'Some_fish_text'
        })
        entry = Entry.objects.get(title='TestEntryNew')
        self.assertEqual(entry.content, 'Some_fish_text')
        self.assertEqual(entry.author.username, 'TestUser')