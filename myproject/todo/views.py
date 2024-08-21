# todo/views.py
from django.http import HttpResponse
from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

def home(request):
    return HttpResponse("환영합니다! ToDo API에 오신 것을 환영합니다.")
