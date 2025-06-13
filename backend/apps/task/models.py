from django.db import models

from apps.account.models import User
from apps.task.choices import TaskStatus


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1023)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=31, choices=TaskStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update(self, **kwargs):
        for attr in kwargs:
            setattr(self, attr, kwargs[attr])
        self.save(update_fields=kwargs.keys())
