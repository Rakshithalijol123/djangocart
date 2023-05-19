from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Registration(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    no = models.CharField(max_length=12)
    check = models.BooleanField(default=False)

    def __str__(self):
        return self.no


