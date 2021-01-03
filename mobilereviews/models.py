from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class User(AbstractUser):
    pass

class UserRatings(models.Model):
    xuser = models.CharField(max_length=64)
    mobileid = models.IntegerField()

class Mobiles(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    link = models.CharField(max_length=1000,default=None,blank=True,null=True)
    rating = models.FloatField( 
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    rcount = models.IntegerField(default=1)