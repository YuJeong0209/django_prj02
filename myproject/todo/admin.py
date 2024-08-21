# todo/admin.py
from django.contrib import admin
from .models import ToDo

@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed')
    # 'completed' 필드를 추가할 수도 있습니다. 필요에 따라 조정합니다.
