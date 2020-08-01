from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializers Name Field Testing"""
    name= serializers.CharField(max_length=10)
