# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Garante que o perfil é criado quando um novo usuário é criado
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

from django.db.models.signals import post_save
post_save.connect(create_user_profile, sender=User)

class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='items/', blank=True, null=True)

    def __str__(self):
        return self.name