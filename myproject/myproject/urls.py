# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import ToDoViewSet

router = DefaultRouter()
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 'api/' 경로에 'todos'를 포함합니다.
    path('', include('todo.urls')),       # 루트 URL을 'todo' 앱의 URL로 포함합니다.
]
