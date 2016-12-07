from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_embalase


class EmbalaseListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:embalase')
        create_user()

    def test_post(self):
        post_data = dict(
            name='Name',
            price=10,
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


class EmbalaseDetailTest(APITestCase):

    def setUp(self):
        embalase = create_embalase()
        self.url = reverse('api:embalase-detail', kwargs=dict(pk=(embalase.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            name='Name',
            price=10,
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


class GetEmbalaseByNameTest(APITestCase):

    def setUp(self):
        create_embalase(name='name')
        self.url = reverse('api:product-by-name', kwargs=dict(name='name'))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
