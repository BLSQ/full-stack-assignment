from rest_framework import serializers

from .models import Todo


class TodoSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'release', 'status', 'date', 'text')
