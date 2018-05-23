from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.TextField(null=True, max_length=60, blank=True)
    mail = models.TextField(null=True, max_length=30, blank=True)
    location = models.CharField(null=True, max_length=30, blank=True, default="Россия")

    birth_date = models.DateField(null=True, blank=True)
    male = models.TextField(null=True, max_length=30, blank=True)

    Shengen = models.BooleanField(default=False)
    SHA = models.BooleanField(default=False)
    China = models.BooleanField(default=False)
    Asia = models.BooleanField(default=False)
    Avstraliya = models.BooleanField(default=False)
    Angliya = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()