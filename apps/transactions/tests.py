from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from apps.accounts.models import User
from apps.transactions.models import Income, Expense


class TransactionsAPITestCase(APITestCase):
    def setUp(self):
        # Crear un jefe
        self.boss = User.objects.create_user(
            username='boss_user',
            email='boss@example.com',
            password='password123',
            role='boss'
        )

        # Crear un taxista asociado al jefe
        self.driver = User.objects.create_user(
            username='driver_user',
            email='driver@example.com',
            password='password123',
            role='driver',
            boss=self.boss
        )

        # Autenticar al taxista
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': self.driver.username,
            'password': 'password123',
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_income(self):
        url = reverse('income-list')
        data = {
            'amount': 100.50,
            'payment_method': 'cash',
            'description': 'Viaje largo'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Income.objects.count(), 1)
        self.assertEqual(Income.objects.first().user, self.driver)

    def test_income_access_restriction(self):
        other_driver = User.objects.create_user(
            username='other_driver',
            email='other_driver@example.com',
            password='password123',
            role='driver'
        )
        Income.objects.create(user=other_driver, amount=100.00, payment_method='cash')
        url = reverse('income-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_expense(self):
        url = reverse('expense-list')
        data = {
            'amount': 30.00,
            'category': 'Gasolina',
            'description': 'Carga de combustible'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(Expense.objects.first().user, self.driver)

    def test_expense_access_restriction(self):
        other_driver = User.objects.create_user(
            username='other_driver',
            email='other_driver@example.com',
            password='password123',
            role='driver'
        )
        Expense.objects.create(user=other_driver, amount=50.00, category='Gasolina')
        url = reverse('expense-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_income_assigns_user(self):
        url = reverse('income-list')
        data = {
            'amount': 100.50,
            'payment_method': 'cash',
            'description': 'Viaje largo'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        income = Income.objects.first()
        self.assertEqual(income.user, self.driver)  # Verifica que se asignó el usuario autenticado

    def test_create_expense_assigns_user(self):
        url = reverse('expense-list')
        data = {
            'amount': 50.00,
            'category': 'Gasolina',
            'description': 'Carga de combustible'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        expense = Expense.objects.first()
        self.assertEqual(expense.user, self.driver)  # Verifica que se asignó el usuario autenticado
