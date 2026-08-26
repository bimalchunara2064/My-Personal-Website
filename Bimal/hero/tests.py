from django.test import SimpleTestCase
from django.urls import reverse


class HeroUrlTests(SimpleTestCase):
    def test_photos_url_name_exists(self):
        self.assertEqual(reverse('photos'), '/photos/')
