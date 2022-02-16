from django.test import TestCase
from summaryApp.models import Document
import os
# import nltk
# nltk.download('punkt')

class SumyTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.text_file = str(open(f'{os.path.abspath(os.path.dirname(__name__))}/summaryApp/tests/text.txt','r').read())
        Document.objects.create(text=cls.text_file)
        
    def test_LexRank(self):
        document = Document.objects.first()
        print("\nLexRank\n\n", document.normalize_sentences(document.summarize_sumy_LexRank()))

    def test_Luhn(self):
        document = Document.objects.first()
        print("\nLuhn\n\n", document.normalize_sentences(document.summarize_sumy_Luhn()))

    def test_LSA(self):
        document = Document.objects.first()
        print("\nLSA\n\n", document.normalize_sentences(document.summarize_sumy_LSA()))
