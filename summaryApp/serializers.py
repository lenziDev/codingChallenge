from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from summaryApp.models import Document

class DocumentRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('text','summary')

class DocumentCreateSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    
    class Meta:
        model = Document
        fields = ('id','text',)