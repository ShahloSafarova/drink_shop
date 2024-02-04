from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
  phone = models.CharField(max_length=13)
  user_image = models.ImageField(default='media/default_users_image.png', upload_to='media/users_images')

  def __str__(self):
    return self.username

  class Meta:
    db_table = 'users_customer'
# Create your models here.
