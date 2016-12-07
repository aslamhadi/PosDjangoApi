from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase

from tests.factories import create_user, create_doctor


class DoctorListTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:doctor')
        create_user()

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data={}, format='json')
        self.assertEqual(response.status_code, 405)


class DoctorDetailTest(APITestCase):

    def setUp(self):
        doctor = create_doctor()
        self.url = reverse('api:doctor-detail', kwargs=dict(pk=str(doctor.id)))
        create_user()

        self.doctor = doctor

    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        post_data = dict(
            city='City',
            address='Address',
            phone_number='123456',
        )

        response = self.client.put(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.put(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, 204)


class DoctorCreateTest(APITestCase):

    def setUp(self):
        self.url = reverse('api:doctor-create')
        create_user()

    def test_post(self):
        post_data = dict(
            username='userdoctor',
            first_name='the doctor',
            city='city',
            address='address',
            phone_number='123456',
        )

        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.post(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_put(self):
        user = create_user(username='userdoctor')
        create_doctor(user=user)
        post_data = dict(
            username='userdoctor',
            first_name='the doctor',
            city='city',
            address='address',
            phone_number='123456',
        )

        response = self.client.put(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 403)

        self.client.login(username='username', password='password')
        response = self.client.put(self.url, data=post_data, format='json')
        self.assertEqual(response.status_code, 200)
