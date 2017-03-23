from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


class Report(models.Model):

    """
Location
user-supplied keyword

private reports cant be searchable or wisable in any way to users accept if they are SM user
Can only be deleted by SM user
    """

    timestamp = models.DateTimeField(default=timezone.now)
    Company_name = models.CharField(max_length=60)
    Company_phone = models.CharField(max_length=12)
    Company_Location = models.CharField(max_length=60)
    country = CountryField()
    sector = models.CharField(max_length=60)
    Industry = models.CharField(max_length=60)
    current_projects = models.TextField()
    file = models.FileField(blank = True)
    encrypted = model.BooleanField(blank = True)
    private = models.BooleanField()



    def __str__(self):
        return self.title
