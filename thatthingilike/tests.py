from django.test import TestCase

class IndexTests(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)