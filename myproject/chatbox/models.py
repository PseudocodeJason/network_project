from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50,help_text="The user name")

class Chatmessage(models.Model):
    message_text = models.CharField(max_length=500, help_text="The message text")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="The timestamp of sending message text")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Response(models.Model):
    response_text = models.CharField(max_length=500,help_text="The response_text")
    message = models.ForeignKey(Chatmessage,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True,help_text="The timestamp of sending message text")
