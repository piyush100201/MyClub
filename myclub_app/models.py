from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=500)
    address = models.CharField(max_length=2000)
    zip_code = models.CharField(max_length=6)
    phone_no = models.CharField(max_length=15,blank=True)
    email = models.EmailField(blank=True)
    owner = models.IntegerField("Venue Owner",blank=False,default=1)

    def __str__(self):
        return self.name


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=500)
    event_date = models.DateTimeField()
    #venue = models.CharField(max_length=500)
    venue = models.ForeignKey(Venue, blank=True,null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
