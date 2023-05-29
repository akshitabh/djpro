from .models import Emp
from rest_framework import viewsets
from .Empserializer import Empserializer
class EmpViewset(viewsets.ModelViewSet):
    queryset=Emp.objects.all()
    serializer_class=Empserializer