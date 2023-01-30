from rest_api.api.serializers import BookListSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .pagination import CustomPagination
from django.http import HttpResponse
from rest_framework import viewsets
from rest_api.models import Books
from rest_framework import status
from random import sample



class BookList(APIView):
    def get(self, request):
        books = Books.objects.all()
        page_number = self.request.query_params.get('page_number', 1)
        page_size = self.request.query_params.get('page_size', 3)

        paginator = Paginator(books , page_size)
        serializer = BookListSerializer(paginator.page(page_number), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class BookDetail(APIView):
    def get(self, request, pk, format=None):
        try:
            book = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response({'Error': 'Book not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookListSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        try:
            book = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response({'Error': 'Book not found'},status=status.HTTP_404_NOT)
        
        serializer = BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
    
        
