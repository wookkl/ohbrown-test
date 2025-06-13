from rest_framework import status
from rest_framework.test import APITestCase

from apps.account.dto import AuthSignUpCommand
from apps.account.services import user_create
from apps.account.utils import get_token_by_user


class UserApiTest(APITestCase):
    def test_mine(self):
        user = user_create(command=AuthSignUpCommand(
            username='honggildong', first_name='보고', last_name='장', password='testpw0511!@'
        ))
        token = get_token_by_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access}')
        resp = self.client.get('/users/mine')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['username'], user.username)
        self.assertEqual(resp.data['first_name'], user.first_name)
        self.assertEqual(resp.data['last_name'], user.last_name)


class AuthApiTest(APITestCase):
    def create_user(self, username, first_name='보고', last_name='장', password='testpw0511!@'):
        return user_create(command=AuthSignUpCommand(
            username=username, first_name=first_name, last_name=last_name, password=password
        ))

    def test_sign_up(self):
        data = {
            'username': 'honggildong',
            'first_name': '길동',
            'last_name': '홍',
            'password': 'qwerty123!',
            'password2': 'qwerty123!',
        }
        resp = self.client.post('/auth/sign-up', data=data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)

    def test_sign_up_invalid_passwords(self):
        # passwords do not match
        data = {
            'username': 'honggildong',
            'first_name': '길동',
            'last_name': '홍',
            'password': 'qwerty123!',
            'password2': 'qwerty123!!',
        }
        resp = self.client.post('/auth/sign-up', data=data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        # only numeric
        data['password'] = '123123'
        data['password2'] = '123123'
        resp = self.client.post('/auth/sign-up', data=data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        # too common
        data['password'] = 'qwerty12'
        data['password2'] = 'qwerty12'
        resp = self.client.post('/auth/sign-up', data=data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        self.user = self.create_user(username='honggildong', password='drowssap2025@')
        data = {
            'username': 'honggildong',
            'password': 'drowssap2025@',
        }
        resp = self.client.post('/auth/login', data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in resp.data)
        self.assertTrue('refresh' in resp.data)
