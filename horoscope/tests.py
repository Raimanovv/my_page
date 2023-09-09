from django.test import TestCase

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
        response = self.client.get('/horoscope/5/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/leo/')
