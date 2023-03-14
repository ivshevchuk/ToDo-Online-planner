from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from ToDo.models import Task


class TaskModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test description',
            author=self.user
        )

    def test_task_created(self):
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_absolute_url(self):
        url = reverse('task_detail', args=[str(self.task.id)])
        self.assertEqual(self.task.get_absolute_url(), url)

    def test_task_author(self):
        self.assertEqual(self.task.author, self.user)
