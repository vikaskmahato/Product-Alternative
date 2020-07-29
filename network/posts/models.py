from django.db import models
from django.core.validators import FileExtensionValidator
from accounts.models import Profile
# Create your models here.

class Post(models.Model):
    content=models.TextField(blank=True)
    image=models.ImageField(upload_to="", validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    created=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    objects=models.Manager()


    


