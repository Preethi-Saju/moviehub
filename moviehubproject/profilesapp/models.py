from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from moviesapp.models import Movie,Category
from django.utils import timezone
User=get_user_model()

class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # profileimg=models.ImageField(upload_to='profile_images',default='blankprofile.png')

    def __str__(self):
        return self.user.username


