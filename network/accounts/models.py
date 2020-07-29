from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    desc=models.TextField(default="No Description", max_length=300)
    contact_details=models.TextField(max_length=300)
    photo=models.ImageField(default="avatar.png" ,  upload_to='' )
    category=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    objects=models.Manager()

    def __str__(self):
        return f"{self.user.username}"



    



