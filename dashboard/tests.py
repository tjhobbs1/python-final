from django.test import TestCase


class TestCase(TestCase):
    def test_dashboard_page_status(self):
        """Check that a connection is made to the dashboard"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_postflight_page_status(self):
        """Check that a connection is made to the postflight"""
        response = self.client.get('/postflight/')
        self.assertEqual(response.status_code, 200)

# Create your tests here.
