from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_factory


class FactoryListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:factory')
        create_user()

    def test_post(self):
        post_data = dict(
            name='Name',
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


class FactoryDetailTest(APITestCase):

    def setUp(self):
        factory = create_factory()
        self.url = reverse('api:factory-detail', kwargs=dict(pk=str(factory.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            name='Name',
        )

        # unauthorized
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.put(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        # unauthorized
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, 204)

