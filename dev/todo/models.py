from django.db import models
import datetime
# Create your models here.

class Todo(models.Model):
    release = models.TextField(max_length=100, null=False)
    status = models.IntegerField(null=False)
    date = models.DateTimeField(null=False)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.release