from django.urls import reverse, path, include
from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"email": "test@localhost.app",
                "password1": "some_strong_psw", "password2": "some_strong_psw"}
        response = self.client.post(
            '/stocka_api/v1/rest-auth/registration/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class AccountTests(APITestCase):

    def test_create_account(self):
        data = {"email": "test@localhost.app",
                "password1": "some_strong_psw", "password2": "some_strong_psw"}
        response = self.client.post(
            '/stocka_api/v1/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
