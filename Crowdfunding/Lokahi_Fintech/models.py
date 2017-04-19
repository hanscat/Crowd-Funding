from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.



class Investor(models.Model):
    name = models.CharField(max_length=100)


class Document(models.Model):
    #report = models.ForeignKey(Report, null=True)
    name = models.CharField(max_length=100, null=True, default=None, blank=True)
    encrypted = models.BooleanField(default=False)
    file = models.FileField(upload_to='documents')
    def __str__(self):
        return str(self.file)


class Report(models.Model):
    date = models.CharField(default=datetime.date.today, max_length=200)
    title = models.CharField(max_length=100, default="")
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    types = (('C',"Company"),("I","Investor"),("N/A",'not declared'))
    role = models.CharField(max_length=20, choices=types)
    
    def __str__(self):
        return self.user.username
    
class Messages(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")
    msg_content = models.CharField(max_length=1000)


class Group(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default="")
    participants = models.ManyToManyField(User)
    #reports = models.ManyToManyField(Report)
    def __str__(self):
        return str(self.name)

    def users(self):
        return self.owner | self.participants

    def is_member(self, user):
        if user == self.owner or user in self.participants:
            return True
        else:
            return False


