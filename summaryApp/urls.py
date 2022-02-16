from summaryApp import views
from django.urls import path

urlpatterns = [
      path('document/', views.DocumentAPIView.as_view(), name='createDocument'),
      path('document/<int:pk>/', views.DocumentUniqueAPIView.as_view(), name='retrieveDocument')
]