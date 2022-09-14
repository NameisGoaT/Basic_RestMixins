from rest_framework import serializers
from .models import Students

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Students