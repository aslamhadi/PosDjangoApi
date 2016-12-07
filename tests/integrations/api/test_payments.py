from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_payment


class CreatePaymentTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:create-payment')
        create_user()

    def test_post(self):
        post_data = dict(
            invoice_number='123',
            total=10,
            cash=10,
            change=10,
        )

        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 201)


class PaymentListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:payment')
        create_user()

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)


class PaymentDetailTest(APITestCase):

    def setUp(self):
        payment = create_payment()
        self.url = reverse('api:payment-detail', kwargs=dict(pk=str(payment.id)))
        create_user()

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            invoice_number='123',
            total=10,
            cash=10,
            change=10,
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
