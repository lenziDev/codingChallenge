from django.test import TestCase, Client
from django.urls import reverse
import os
from summaryApp.models import Document

class TestViews(TestCase):

    def document_creation(self):
        return Document.objects.create(text=self.text_file) 

    def setUp(self):
        self.client = Client()
        self.text_file = str(open(f'{os.path.abspath(os.path.dirname(__name__))}/summaryApp/tests/text.txt','r').read())
        self.document_creation()

    def test_create_document(self):
        response = self.client.post(reverse('createDocument'), {"text": self.text_file})
        self.assertEquals(response.status_code, 201)

    def test_retrieve_document(self):
        response = self.client.get(f"/document/{self.document_creation().id}/")
        self.assertEquals(response.status_code, 200)