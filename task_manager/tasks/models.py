from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    due_date = models.DateTimeField(null=True)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=6, default='medium')
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, default='pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='task_updated_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title
