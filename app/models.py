
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    #user = models.ForeignKey(User, models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    canister = models.IntegerField()
    created = models.DateTimeField(default=timezone.now())
    fragrance_type = models.CharField(max_length=50)

    def __repr__(self) -> str:
        return super().__repr__()
    

class MedicalCondition(models.Model): 
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500, default=None)
    created = models.DateTimeField(default=timezone.now())

class UserMedicalCondition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.ForeignKey(MedicalCondition, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now())
