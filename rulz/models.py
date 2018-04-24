from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Rulz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    country = models.CharField(max_length=255,default='France')
    city = models.CharField(max_length=255,default='Paris')
    player_num = models.IntegerField(default=2)
    complexity = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)



    def get_absolute_url(self):
        return reverse('rulz:rulz_detail',kwargs={'pk':self.pk})
