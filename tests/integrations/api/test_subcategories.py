from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_category, create_subcategory


class SubCategoryListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:subcategory')
        self.category = create_category()
        create_user()

    def test_post(self):
        post_data = dict(
            category=self.category.id,
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


class SubCategoryDetailTest(APITestCase):

    def setUp(self):
        subcategory = create_subcategory()
        self.category = subcategory.category
        self.url = reverse('api:subcategory-detail', kwargs=dict(pk=str(subcategory.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            category=self.category.id,
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


class SubCategoryInCategoryTest(APITestCase):

    def setUp(self):
        subcategory = create_subcategory()
        category = subcategory.category
        self.url = reverse('api:subcategory-in-category', kwargs=dict(pk=str(category.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
