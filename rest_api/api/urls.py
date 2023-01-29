from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.api.views import BookListAV, BookList

router = DefaultRouter()

urlpatterns = [
    path('list/', BookListAV.as_view(), name='book_list'),
    path('listnew/', BookList.as_view(), name='book'),
    path('', include(router.urls)),
]
