from django.test import TestCase, Client
from .models import College
import json


cl = Client()

class CollegeTest(TestCase):
    def setUp(self):
        id = 0
        name = 'Computer Science'
        self.college = College.objects.create(name="Computer Science", contact="0113075979", location="Al Kadaro, Bahri, Khartoum")
        self.college1 = College.objects.create(name="Engineering", contact="0905599319", location="Al Kadaro, Bahri, Khartoum")
        self.colleges = College.objects.all().values()

    def test_college_fields(self):
        self.assertIsNotNone(self.college.name, "College Name not found")
        self.assertIsNotNone(self.college.contact, "College Contact not found")
        self.assertIsNotNone(self.college.location, "College Location not found")
    
    def test_get_college_endpoint(self):
        response = cl.get(f'/colleges/{self.college.id}/')
        self.assertEqual(response.status_code, 200) #TODO Get Details and check them
        
    def test_list_colleges_endpoint(self):
        response = cl.get('/colleges/') #TODO Test the endpoint Body and the College List 
        self.assertEqual(self.colleges.__str__(), response.json())

        self.assertEqual(response.status_code, 200)
    
    def test_college_name_uniqe(self): #TODO Another test
        
        try :
            from django.db.utils import IntegrityError
            College.objects.create(name="Engineering", contact="0905599319", location="Al Kadaro, Bahri, Khartoum")
        except Exception as e:
            self.assertEqual(e.__str__(), 'UNIQUE constraint failed: college_college.name')
        
