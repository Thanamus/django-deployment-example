from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    #creating one to one relationship to User model in .auth.models

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(blank=True)

    # portfolio_pic = models.ImageField(upload_to='profile_pic',blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',blank=True)


    def __str__(self):
        return self.user.username
