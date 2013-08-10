from django.contrib import admin
from models import tasks

class TaskAdmin(admin.ModelAdmin):
    fields = ('status', 'task')
admin.site.register(tasks, TaskAdmin)