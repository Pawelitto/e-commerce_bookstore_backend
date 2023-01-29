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



class BookListAV(ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookListSerializer
    pagination_class = CustomPagination


class BookList(APIView):

    def get(self, request, format=None):
        books = BookList.objects.all()
        serializer = BookListSerializer(books, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request):
    #     books = BookList.objects.all()
    #     page_number = self.request.query_params.get('page_number ', 1)
    #     page_size = self.request.query_params.get('page_size ', 10)

    #     paginator = Paginator(books , page_size)
    #     serializer = BookListSerializer(paginator.page(page_number), many=True)

    #     return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    
        
