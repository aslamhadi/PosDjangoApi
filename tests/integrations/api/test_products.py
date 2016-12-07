from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_product, create_category, create_factory, create_unit_type


class ProductListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:product')
        create_user()

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)


class ProductDetailTest(APITestCase):

    def setUp(self):
        product = create_product()
        self.url = reverse('api:product-detail', kwargs=dict(pk=str(product.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        category = create_category()
        unit_type = create_unit_type()
        factory = create_factory()
        post_data = dict(
            name='Name',
            price=10,
            barcode='barcode',
            category=category.id,
            unit_type=unit_type.id,
            factory=factory.id,
        )

        # unauthorized
        response = self.client.put(self.url, data=post_data, format='json')
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


class ProductCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse('api:product-create')
        create_user()

    def test_post(self):
        category = create_category()
        unit_type = create_unit_type()
        factory = create_factory()
        post_data = dict(
            name='Name',
            price=10,
            barcode='barcode',
            category=category.id,
            unit_type=unit_type.id,
            factory=factory.id,
        )

        # unauthorized
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 405)


class GetProductsByNameTest(APITestCase):

    def setUp(self):
        product = create_product()
        self.url = reverse('api:product-by-name', kwargs=dict(name=product.name))
        create_user()

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.login(username='username', password='password')
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, 405)