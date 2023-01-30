from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.api.views import BookList, BookDetail

router = DefaultRouter()

urlpatterns = [

    path('books', BookList.as_view(), name='book_list'),
    path('books/<int:pk>', BookDetail.as_view(), name='book_detail'),
    
    path('', include(router.urls)),
]
