from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user


class UserListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:user')
        create_user()

    def test_post(self):
        post_data = dict(
            username='newusername',
            email='newuser@email.com',
            first_name='Name',
            is_staff=False,
        )

        # unauthorized
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)