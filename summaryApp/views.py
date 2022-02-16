from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

# Create your views here.
class DocumentUniqueAPIView(APIView):
    def get(self, request, pk, format=None):
        try:
            item = Document.objects.get(id=pk)
            serializer = DocumentRetrieveSerializer(item)
            return Response(serializer.data)
        except Document.DoesNotExist:
            return Response(status=404)

class DocumentAPIView(APIView):
    def post(self, request, format=None):
        serializer = DocumentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=201)
            return response
        return Response(serializer.errors, status=400)