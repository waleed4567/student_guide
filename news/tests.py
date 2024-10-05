from django.test import TestCase
from django.test import Client

client = Client(HTTP_USER_AGENT='Mozilla/5.0')

class NewsTest(TestCase):
    def setUp(self):
        pass # No setup needed for now

    def test_new_post(self):
        response = client.get('/news/new/')
        self.assertEqual(response.status_code, 200)
        #raise AssertionError('Not_Implemented Implement this feature')

    def test_get_posts(self):
        response = client.get('/news/')
        self.assertEqual(response.status_code, 200)
        #raise AssertionError('Not_Implemented Implement this feature')

    def test_notify_users(self):
        response = client.get('/ws/news/notification/')
        self.assertEqual(response.status_code, 200)
        #raise AssertionError('Not_Implemented Implement this feature')

    def test_interact_with_post(self):
        response = client.get('/ws/news/interract/')
        self.assertEqual(response.status_code, 200)
        #raise AssertionError('Not_Implemented Implement this feature')

    def test_other_features(self):
        response = client.get('/news/article/', follow=True)
        self.assertEqual(response.status_code, 200)
        # TODO Add other features and so on
        #raise AssertionError('Not_Implemented Implement this feature')
    
