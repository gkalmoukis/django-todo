from django.test import TestCase
from rest_framework.test import APIClient

class TaskTestCase(TestCase):
    def test_home_endpoint(self):
        client = APIClient()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_task_index_endpoint(self):
        client = APIClient()
        response = client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
    