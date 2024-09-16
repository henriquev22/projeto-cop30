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
    CONDITION_CHOICES = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Reciclavel', 'Reciclavel'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    condition = models.CharField(max_length=12, choices=CONDITION_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title