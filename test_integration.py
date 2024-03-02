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
        # 添加一个新任务
        response = self.client.post('/add', data={
            'title': 'Integration Test Task',
            'content': 'Integration Test Content'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # 验证任务是否被正确添加
        task = Task.query.first()
        self.assertIsNotNone(task)
        self.assertEqual(task.title, 'Integration Test Task')
