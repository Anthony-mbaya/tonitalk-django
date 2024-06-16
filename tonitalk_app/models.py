from django.db import models
from datetime import datetime

# Create your models here.
class ChatRoom(models.Model):
    room_name = models.CharField(max_length=1000)

class ChatMessages(models.Model):
    user_message = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    sender = models.CharField(max_length=100000000)
    user_room = models.CharField(max_length=1000000)
