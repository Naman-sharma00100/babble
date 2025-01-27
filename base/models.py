from django.db import models

# Create your models here.


class Post(models.Model):
    sender = models.CharField(max_length=200, null=True) 
    body = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    channel_id = models.CharField(max_length=16,null=False)
    def __str__(self):
        return self.body[0:50]