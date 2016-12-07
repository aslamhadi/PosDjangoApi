from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_product


class CreatePrescriptionTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:create-prescription')
        create_user()

    def test_post(self):
        products = [create_product() for _ in range(3)]

        post_data = dict(
            products=[product.id for product in products],
            sub_total=10,
        )

        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 201)
