from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

from datetime import date, timedelta, datetime


# Create your models here.

class OneToOne(models.Model):
    user1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_created')
    user2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_reciever') 
    room_name = models.CharField(max_length=100)
    
class Messages(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_sender')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s_requests_reciever')
    onetoone = models.ForeignKey(OneToOne,on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
    message = models.TextField(null=True)
    msg_type = models.CharField(max_length=15,null=True)
    image = models.ImageField(upload_to='files',null=True)
    
    @property
    def get_image(self):
        try:
            return self.image.url
        except:
            return ''