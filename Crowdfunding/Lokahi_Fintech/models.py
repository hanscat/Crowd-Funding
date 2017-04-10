from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.
class report(models.Model):

    """Fields needed:

1. Timestamp when report created (automated date/time the report is created).
2. Company Name. (one line of text)
3. Company Phone. (one line of text)
4. Company Location (one line of text)
5. Company Country (one line of text or a drop down list)
6. Sector (one line or a drop down list)
7. Industry (one line of text or a drop down list)
8. Current Project(s) (multiple lines of text)
9. One or more files (optional, a report does not have to have a file attached however, the option must be
available). Any file format can be uploaded. The user should be able to indicate if the uploaded file is
encrypted. (The system should not encrypt the file or store the information to allow it to be decrypted. But
it must know whether a given file is encrypted or not.)
10. Whether the report is public or private (public reports can be seen by any user of the system, private can
be seen by only those given access).

Location
user-supplied keyword

private reports cant be searchable or wisable in any way to users accept if they are SM user
Can only be deleted by SM user
    """

    timestamp = models.DateTimeField(default=timezone.now)
    Company_name = models.CharField(max_length=60)
    Company_phone = models.CharField(max_length=12)
    Company_Location = models.CharField(max_length=60)
    country = models.CountryField()
    sector = models.CharField(max_length=60)
    Industry = models.CharField(max_length=60)
    current_projects = models.TextField()
    title = models.CharField(max_length=100, default=str(Company_name) + " New Report")
    file = models.FileField(blank = True)
    encrypted = models.BooleanField(blank = True)

    private = models.BooleanField()

    def __str__(self):
        return self.title


class user(models.Model):
    # general purpose user
    first_name = models.CharField(max_length=20, default="new")
    last_name  = models.CharField(max_length=20, default="user")
    user_name = models.CharField(max_length=30, unique = True, default="newUser")
    password = models.CharField(max_length=30, default="password")

    class Meta:
        managed = True

    def __str__(self):
        return self.user_name

import json
from django.contrib.postgres.fields import JSONField

class group(models.Model):
    name = models.CharField(max_length=100, default="new group")
    users = JSONField()
    reports = JSONField()

    #we can decide later whether we want to give groups access to reports here or include
    #which groups get access within the report model, i don't think it makes a big difference. Maybe both.
    #The same principle applies to which users and groups.

    #using the JSONField allows data to be stored in the users field, mainly as a dictionary,
    #so we will have usernames and actual names, as well as possibly permissions all stored
    #in this JSONField. I looked around, and thats the best way to do it.

    def __str__(self):
        return self.name


