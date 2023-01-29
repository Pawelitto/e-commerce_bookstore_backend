from rest_framework import serializers
from rest_api.models import Books


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'