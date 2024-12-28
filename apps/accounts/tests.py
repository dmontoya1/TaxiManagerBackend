from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationTestCase(APITestCase):
    def test_user_registration(self):
        url = '/api/accounts/register/'
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepassword123",
            "password2": "securepassword123",
            "role": "driver",
            "phone": "1234567890"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="securepassword123",
            role="driver"
        )

    def test_user_login(self):
        url = '/api/accounts/login/'
        data = {
            "username": "testuser",
            "password": "securepassword123"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
