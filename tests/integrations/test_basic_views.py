from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase


user_model = get_user_model()


class HomeTest(TestCase):

    def setUp(self):
        self.url = reverse('home')

    def test_get_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_get_authorized(self):
        user_model.objects.create_user('username', 'email@user.com', 'password')
        self.client.login(username='username', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):

    def setUp(self):
        self.url = reverse('login')

    def test_get_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class RegisterTest(TestCase):

    def setUp(self):
        self.url = reverse('register')

    def test_get_unauthorized(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
