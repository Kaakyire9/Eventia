from django.test import TestCase
from .models import Event
from django.contrib.auth.models import User

class EventModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            date='2025-01-01',
            time='12:00:00',
            location='Test Location',
            organizer=self.user
        )

    def test_event_creation(self):
        self.assertEqual(self.event.title, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event')
        self.assertEqual(self.event.location, 'Test Location')
        self.assertEqual(self.event.organizer.username, 'testuser')

    def test_event_str(self):
        self.assertEqual(str(self.event), 'Test Event')

    def test_event_update(self):
        self.event.title = 'Updated Event'
        self.event.save()
        self.assertEqual(self.event.title, 'Updated Event')

    def test_event_deletion(self):
        event_id = self.event.id
        self.event.delete()
        with self.assertRaises(Event.DoesNotExist):
            Event.objects.get(id=event_id)
