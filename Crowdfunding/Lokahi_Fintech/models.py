from django.db import models
import datetime
from django.contrib.auth.models import User, Group


# Create your models here.

# class Group(models.Model):
#     title = models.CharField(max_length=100)
#     participants = models.ManyToManyField()
#     owner = models.OneToOneField()


class Report(models.Model):
    date = models.CharField(default=datetime.date.today, max_length=200)
    title = models.CharField(max_length=100)
    Company = models.CharField(max_length=60)
    Industry = models.CharField(max_length=60)
    encrypted = models.BooleanField(blank = True)
    private = models.BooleanField()

    def __str__(self):
        return self.title
    # timestamp = models.DateTimeField(default=timezone.now)
    # Company_phone = models.CharField(max_length=12)
    # Company_Location = models.CharField(max_length=60)
    # # country = CountryField()
    # sector = models.CharField(max_length=60)
    # current_projects = models.TextField()
    # file = models.FileField(blank = True)


# 
# class User(models.Model):
#     #to store the name of the user
#     username = models.CharField(max_length=100)
#     #to store the email of the user
#     email = models.CharField(max_length=100)
#     #to store the password of the user
#     password = models.CharField(max_length=100)
#     # to store an array of participating groups
#     group = models.ManyToManyField()
    




