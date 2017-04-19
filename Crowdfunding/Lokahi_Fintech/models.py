from django.db import models
import datetime
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    title = models.CharField(max_length=100)
    # participants = models.ManyToManyField(User, db_constraint=True, swappable=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Investor(models.Model):
    name = models.CharField(max_length=100)


class Report(models.Model):
    date = models.CharField(default=datetime.date.today, max_length=200)
    title = models.CharField(max_length=100)
    Company = models.CharField(max_length=60)
    Industry = models.CharField(max_length=60)
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

class File(models.Model):
    report = models.ForeignKey(Report, null=True)
    name = models.CharField(max_length=100, null=True, default=None, blank=True)
    encrypted = models.BooleanField(default=False)
    filename = models.FileField(upload_to='documents')
    def __str__(self):
        return str(self.docfile)

class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    types = (('C',"Company"),("I","Investor"),("N/A",'not declared'))
    role = models.CharField(max_length=20, choices=types)
    
    def __str__(self):
        return self.user.username
