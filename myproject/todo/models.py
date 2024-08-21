# todo/models.py
from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)  # 추가된 필드

    def __str__(self):
        return self.title
