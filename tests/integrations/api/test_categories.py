import os

from django.conf import settings
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_category


CSV_TEST_FILE = os.path.join(settings.BASE_DIR, 'tests', 'data', 'empty.csv')


class CategoryListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:category')
        create_user()

    def test_post(self):
        post_data = dict(
            name='Name',
            idx_sale_price=10,
            idx_sale_price_prescription=10,
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


class CategoryImportCSVTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:category-import-csv')
        create_user()

    def test_post(self):
        with open(CSV_TEST_FILE) as fd:
            post_data = dict(
                file=fd,
            )

            # unauthorized
            response = self.client.post(self.url, data=post_data)
            self.assertEqual(response.status_code, 403)

            self.client.login(username='username', password='password')
            response = self.client.post(self.url, data=post_data)
            self.assertEqual(response.status_code, 201)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)


class CategoryDetailTest(APITestCase):

    def setUp(self):
        category = create_category()
        self.url = reverse('api:category-detail', kwargs=dict(pk=str(category.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            name='Name',
            idx_sale_price=10,
            idx_sale_price_prescription=10,
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
