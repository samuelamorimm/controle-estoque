from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.username