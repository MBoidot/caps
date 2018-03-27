from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Rulz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    player_num = models.IntegerField()
    complexity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('rule_detail', kwargs={'pk': self.pk})
