from django.db import models

class StatusChoices(models.TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in_progress', 'In Progress'
    DONE = 'done', 'Done'

class Todo(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.NEW,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title