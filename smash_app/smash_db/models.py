from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)

class My_User(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='first_name')
    last_name = models.CharField(max_length=120,verbose_name='last_name')
    tag = models.CharField(max_length=30,verbose_name='tag')
    last_login = models.CharField(max_length=30,verbose_name='login',blank=True,null=True)
    tag_id = models.IntegerField(verbose_name='id_tag', null=True)
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    phone = models.CharField(max_length=10, verbose_name='phone', null=True)
    battle_like = models.IntegerField(default=0)
    admin_battle_like = models.IntegerField(default=0)
    likes_users = models.TextField(null=True)
    battle_like_activity = models.IntegerField(default=0)