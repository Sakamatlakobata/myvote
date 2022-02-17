from django.contrib.auth.models import User
from django.db import models

class Accounts(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE,)
    zipcode  = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
