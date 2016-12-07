from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_payment_product, create_product


class PaymentProductDetailTest(APITestCase):

    def setUp(self):
        product = create_product()
        payment_product = create_payment_product(product=product)
        self.url = reverse('api:payment-product-detail', kwargs=dict(pk=str(payment_product.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            product_name='Test',
            price=10,
            discount=1,
            total=10,
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


class GetPaymentProductsByIdTest(APITestCase):

    def setUp(self):
        product = create_product()
        payment_product = create_payment_product(product=product)
        payment = payment_product.payment
        self.url = reverse('api:payment-product-by-payment-id', kwargs=dict(payment=str(payment.id)))
        create_user()

    def test_get(self):
        # unauthorized
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)
