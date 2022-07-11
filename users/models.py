from django.db import models
from django.urls import reverse

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    admin = models.BooleanField(default=False)

    def __str__(self):
        if(self.admin):
            return self.firstname + " " + self.lastname + " (Admin)"
        else:
            return self.firstname + " " + self.lastname

    def get_absolute_url(self):
           return reverse("users:index")