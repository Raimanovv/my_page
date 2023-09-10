from django.test import TestCase
from django.urls import reverse
from .views import zodiac_dict


# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_leo(self):
        response = self.client.get('/horoscope/leo/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('солнце (с 23 июля по 21 августа)', response.content.decode())

    def test_leo_redirect(self):
        for number, zodiac in enumerate(zodiac_dict):
            response = self.client.get(f'/horoscope/{number + 1}/')
            self.assertEqual(response.status_code, 302)
            reverse_path = reverse('horoscope-name', args=(zodiac,))
            self.assertEqual(response.url, reverse_path)

    def test_all_horoscope_content(self):
        zodiacs = zodiac_dict
        for zodiac, description in zodiacs.items():
            reverse_path = reverse('horoscope-name', args=(zodiac,))
            response = self.client.get(reverse_path)
            self.assertEqual(response.status_code, 200)
            self.assertIn(description, response.content.decode())
