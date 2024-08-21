# todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 루트 URL을 처리할 뷰
]
