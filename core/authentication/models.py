from django.db import models
from django.contrib.auth.models import User

#models for tasks and tickets

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    file = models.FileField(upload_to='task_files/', blank=True, null=True)
    priority = models.CharField(max_length=20)
    assigned_user = models.CharField(max_length=20)#ForeignKey(User, on_delete=models.CASCADE)

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20)
    file = models.FileField(upload_to='ticket_files/', blank=True, null=True)
    priority = models.CharField(max_length=20)
    assigned_user = models.CharField(max_length=20)#ForeignKey(User, on_delete=models.CASCADE)