from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.title