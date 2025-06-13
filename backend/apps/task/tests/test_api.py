from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from apps.account.models import User
from apps.task.dto import TaskCreateCommand
from apps.task.models import Task
from apps.task.services import task_create


class TaskApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpw0511!@')
        self.token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def create_sample_task(self, user, title='장보기', description='계란'):
        return task_create(
            user=user, command=TaskCreateCommand(title=title, description=description)
        )

    def test_create(self):
        data = {'title': '장보기', 'description': '계란'}
        resp = self.client.post('/tasks', data=data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data['title'], data['title'])
        self.assertEqual(resp.data['description'], data['description'])
        self.assertEqual(resp.data['status'], 'TODO')
        self.assertTrue('id' in resp.data)
        self.assertTrue('created_at' in resp.data)
        self.assertTrue('updated_at' in resp.data)

    def test_create_anonymous_user(self):
        anonymous_user = APIClient()
        data = {'title': '장보기', 'description': '계란'}
        resp = anonymous_user.post('/tasks', data=data)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list(self):
        other_user = User.objects.create_user(username='otehr_user', password='testpw0511!@')
        self.create_sample_task(user=other_user, title='다른사람할일', description='내용')
        sample_tasks = [
            self.create_sample_task(user=self.user, title=f'할일{num}', description=f'내용{num}')
            for num in range(5)
        ]
        resp = self.client.get('/tasks?page_size=3')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['tasks']), 3)
        self.assertTrue('cursor' in resp.data)
        last_task = sample_tasks[-3]
        resp_last_task = resp.data['tasks'][-1]
        self.assertEqual(last_task.id, resp_last_task['id'])
        self.assertEqual(last_task.title, resp_last_task['title'])
        self.assertEqual(last_task.status, resp_last_task['status'])
        cursor = resp.data['cursor']
        resp = self.client.get(f'/tasks?page_size=3&cursor={cursor}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data['tasks']), 2)

    def test_list_anonymous_user(self):
        anonymous_user = APIClient()
        resp = anonymous_user.get('/tasks?page_size=3')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve(self):
        task = self.create_sample_task(user=self.user)
        resp = self.client.get(f'/tasks/{task.id}')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['title'], task.title)
        self.assertEqual(resp.data['description'], task.description)
        self.assertEqual(resp.data['status'], task.status)
        self.assertEqual(resp.data['id'], task.id)
        self.assertTrue('created_at' in resp.data)
        self.assertTrue('updated_at' in resp.data)

        anonymous_user = APIClient()
        resp = anonymous_user.get(f'/tasks/{task.id}')
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_other_user_raise_404(self):
        task = self.create_sample_task(user=self.user)
        other_user = User.objects.create_user(username='other_user', password='testpw0511!@')
        other_token = AccessToken.for_user(other_user)
        other_client = APIClient()
        other_client.credentials(HTTP_AUTHORIZATION=f'Bearer {other_token}')
        resp = other_client.get(f'/tasks/{task.id}')
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

    def test_partial_update(self):
        task = self.create_sample_task(user=self.user)
        data = {'title': 'new title', 'description': 'new description', 'status': 'DONE'}
        resp = self.client.patch(f'/tasks/{task.id}', data=data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['title'], data['title'])
        self.assertEqual(resp.data['description'], data['description'])
        self.assertEqual(resp.data['status'], data['status'])

    def test_destroy(self):
        task = self.create_sample_task(user=self.user)
        resp = self.client.delete(f'/tasks/{task.id}')
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)
