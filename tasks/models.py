from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='TODO')
    progress = models.IntegerField(default=0)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)

    # 🔔 notification helpers
    def is_overdue(self):
        return self.deadline and self.deadline < timezone.now().date() and self.status != 'DONE'

    def is_due_today(self):
        return self.deadline == timezone.now().date() and self.status != 'DONE'

    def is_due_soon(self):
        if not self.deadline or self.status == 'DONE':
            return False
        delta = (self.deadline - timezone.now().date()).days
        return 0 < delta <= 3

    def __str__(self):
        return self.title
