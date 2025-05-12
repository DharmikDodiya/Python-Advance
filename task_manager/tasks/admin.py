from django.contrib import admin
from .models import Task
# Register your models here.
# Third Why
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'priority', 'user')