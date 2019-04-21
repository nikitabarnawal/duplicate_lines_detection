from django.test import TestCase, Client
from django.urls import reverse

class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_returns_success_response(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_upload(self):
        url = reverse('upload')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


        