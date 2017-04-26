from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_investor = models.BooleanField(default=False) # True for investor, false for company user
    company = models.CharField(max_length=100, null=True)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


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
    name = models.CharField(max_length=100, default="")
    reports = models.ForeignKey('Report', null=True)
    encrypted = models.BooleanField(default=False)
    encryptionKey = models.CharField(max_length=100, default="", blank=True)
    filename = models.FileField(upload_to='documents', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'file'


class Group1(models.Model):
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    participants = models.ManyToManyField(User)

    # reports = models.ManyToManyField(Report)
    def __str__(self):
        return str(self.title)

    def people(self):
        return self.owner | self.participants

    def is_member(self, member):
        if member == self.owner or member in self.participants:
            return True
        else:
            return False

    class Meta:
        db_table = 'groups1'


class Report(models.Model):
    owner = models.CharField(max_length=60, default="")
    date = models.CharField(default=datetime.date.today, max_length=200)
    title = models.CharField(max_length=100, default="")
    company = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=12, default="")
    location = models.CharField(max_length=60, default="")
    country = models.CharField(max_length=60, default="")
    industry = models.CharField(max_length=60, default="")
    sector = models.CharField(max_length=60, default="")
    projects = models.TextField(default="")
    files = models.ManyToManyField(File, blank=True)
    viewers = models.ManyToManyField(User, blank=True)
    groups = models.ManyToManyField(Group1, blank=True)
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

    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        db_table = 'report'



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    content = models.TextField(max_length=500)
    time = models.DateField(default=None, blank=True, null=True)
    to_encrypt = models.BooleanField(default=False)
    key = models.TextField(max_length=10000, null=True, blank=True)
