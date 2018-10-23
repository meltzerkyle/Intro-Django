from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)

class PersonalNote(Note):
    user = models.ForeignKey(User, on_delete=models.CASCADE)