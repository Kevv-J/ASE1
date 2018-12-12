from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from organiser_app.models import *

from django.urls import reverse


class TestCandidate(TestCase):

    @classmethod
    def setUpTestData(cls):
        candidate = Candidate.objects.create(candidate_name='deepesh', candidate_dob = '1998-10-10',candidate_email="deepesh.b17@gmail.com",candidate_fname="ashok",candidate_party="BJP",candidate_region="0",candidate_gender="M",candidate_aadhar=123456321)

    def test_candidate(self):
        candidate = Candidate.objects.get(candidate_id = 1)
        self.assertEquals(candidate.candidate_name,'deepesh')

class TestView(TestCase):
     @classmethod
     def setUpTestData(cls):
        cls.client = Client()

     def test_view_index(self):
         response = self.client.get(reverse('organiser_app:index'))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'organiser_app/index.html')
