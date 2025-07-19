from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerialzer
class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerialzer
# Create your views here.
