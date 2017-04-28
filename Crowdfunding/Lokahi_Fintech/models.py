from django.db import models
import datetime
from django.contrib.auth.models import User



# Create your models here.



class Investor(models.Model):
    name = models.CharField(max_length=100)


class Document(models.Model):
    report = models.ForeignKey('Report', null=True)
    name = models.CharField(max_length=100, null=True, default=None, blank=True)
    encrypted = models.BooleanField(default=False)
    file = models.FileField(upload_to='documents')
    def __str__(self):
        return str(self.file)

    class Meta:
        db_table = 'document'


class File(models.Model):

    #name = models.CharField(max_length=100, default="")
    #reports = models.ForeignKey('Report', null = True)
    #encrypted = models.BooleanField(default=False)
    #encryptionKey = models.CharField(max_length=100, default="", blank=True)
    file = models.FileField(upload_to='Lokahi_Fintech/static/documents/', blank=True)
    actualurl=models.TextField(default="")
    #def __str__(self):
        #return str(self.name)

    class Meta:
        db_table = 'file'

class Report(models.Model):

    OPTIONS=(('Y', 'Yes'),
             ('N', 'No'),)
    title = models.CharField(max_length=100, default="")
    company = models.CharField(max_length=60, default="")
    owner = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=12, default="")
    location = models.CharField(max_length=60, default="")
    country = models.CharField(max_length=60, default="")
    industry = models.CharField(max_length=60, default="")
    sector = models.CharField(max_length=60, default="")
    projects = models.TextField(default="")
    created_at = models.DateTimeField('Date Created', default=datetime.datetime.now)
    #files = models.ManyToManyField(File, blank=True)
    files = models.ManyToManyField(File, default="none")
    is_private = models.NullBooleanField(default=False)
    is_encrypted = models.NullBooleanField(default=False)


    def __str__(self):
        return self.title
        # timestamp = models.DateTimeField(default=timezone.now)
        # Company_phone = models.CharField(max_length=12)
        # Company_Location = models.CharField(max_length=60)
        # # country = CountryField()
        # sector = models.CharField(max_length=60)
        # current_projects = models.TextField()
        # file = models.FileField(blank = True)
    class Meta:
        db_table = 'report'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    types = (('C',"Company"),("I","Investor"),("N/A",'not declared'))
    role = models.CharField(max_length=20, choices=types)
    
    def __str__(self):
        return self.user.username


class Group1(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100, default="")
    participants = models.ManyToManyField(User)
    #reports = models.ManyToManyField(Report)
    def __str__(self):
        return str(self.name)

    def people(self):
        return self.owner | self.participants

    def is_member(self, member):
        if member == self.owner or member in self.participants:
            return True
        else:
            return False
    class Meta:
        db_table = 'groups1'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.TextField(max_length=500)
    time = models.DateField(default=None, blank=True,null=True)
    to_encrypt = models.BooleanField(default=False)
    key = models.TextField(max_length=10000, null=True, blank=True)
     
