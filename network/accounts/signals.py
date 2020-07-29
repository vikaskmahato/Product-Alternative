from django.db.models.signals import post_save
from django.contrib.auth.models import User       #sender
#for registering signals, receiver decorator
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def post_save_createprofile(sender, instance, created, **kwargs):  #instance of particular user, created=bool
    
    if created:
        Profile.objects.create(user=instance)    


