from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Chat(models.Model):
    message = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
