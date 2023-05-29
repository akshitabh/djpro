from rest_framework import serializers
from .models import Emp
class Empserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Emp
        fields = ['id', 'ename', 'address', 'email']