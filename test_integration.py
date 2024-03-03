# test_integration.py
from app import create_app, db
from app.models import Task
import unittest

class IntegrationTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_task_flow(self):
# Add a new task
        response = self.client.post('/add', data={
            'title': 'Integration Test Task',
            'content': 'Integration Test Content'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
# Verify that the task was added correctly
        task = Task.query.first()
        self.assertIsNotNone(task)
        self.assertEqual(task.title, 'Integration Test Task')
