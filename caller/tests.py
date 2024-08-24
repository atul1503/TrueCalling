import urllib.parse
from caller.models import UserPhoneLabelMapping
from caller.generate_test_records import UserPhoneLabelMappingRecords
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
import json

class UserPhoneLabelMappingTestSuite(APITestCase):

    @classmethod
    def setUpTestData(cls):
        UserPhoneLabelMappingRecords.run()

    def setUp(self):
        self.client=APIClient()
        self.url=reverse('token_obtain_pair')
        data={
            'username':'testuser',
            'password':'testuser',
            'phonenumber':'5955954933'
        }
        response=self.client.post(self.url,data,format='json')
        output=json.loads(str(response.content.decode("utf-8")))
        token=output.get('token','')
        self.headers={
            'HTTP_AUTHORIZATION': 'Token '+token
        }

    def test_report_case1(self):
        phonnumber="12345678910"
        data={
            "phonenumber": phonnumber,
            "label": "SPAM"
        }
        self.url=reverse('reports')
        response1=self.client.post(self.url,data,format='json',**self.headers)
        self.assertEqual(response1.status_code,200) and self.assertContains(UserPhoneLabelMapping.objects.filter(phonenumber=phonnumber),"SPAM")

    def test_report_case2(self):
        phonnumber="12345678910"
        data={
            "phonenumber": phonnumber,
            "label": "VERIFIED"
        }
        self.url=reverse('reports')
        response1=self.client.post(self.url,data,format='json',**self.headers)
        self.assertEqual(response1.status_code,200) and self.assertContains(UserPhoneLabelMapping.objects.filter(phonenumber=phonnumber),"VERIFIED")

    def test_report_case3(self):
        phonnumber="1234567896"
        data={
            "phonenumber": phonnumber,
            "label": "VERIFIED"
        }
        self.url=reverse('reports')
        response1=self.client.post(self.url,data,format='json',**self.headers)
        (self.assertEqual(response1.status_code,200))  and self.assertContains(UserPhoneLabelMapping.objects.filter(phonenumber=phonnumber),"VERIFIED")

    def test_search_case1(self):
        
        base_url = reverse('name_search')
        query_params = urllib.parse.urlencode({'fullname': 'Atul'})
        self.url = f"{base_url}?{query_params}"
        response=self.client.get(self.url,**self.headers)
        self.assertContains(response,"Atul")

    def test_search_case2(self):
        base_url = reverse('name_search')
        query_params = urllib.parse.urlencode({'fullname': 'John'})
        self.url = f"{base_url}?{query_params}"
        response=self.client.get(self.url,**self.headers)
        self.assertContains(response,"Bharat")

    def test_search_case4(self):
        phonenumber="12345678910"
        base_url=reverse("phone_search")
        query_params = urllib.parse.urlencode({'phonenumber': phonenumber})
        self.url = f"{base_url}?{query_params}"
        response=self.client.get(self.url,**self.headers)
        self.assertContains(response,"Atul")

    def test_search_case5(self):
        phonenumber="1234567891"
        base_url=reverse("phone_search")
        query_params = urllib.parse.urlencode({'phonenumber': phonenumber})
        self.url = f"{base_url}?{query_params}"
        response=self.client.get(self.url,**self.headers)
        self.assertContains(response,"John")

    

