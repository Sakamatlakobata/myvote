from django.db import models

class Venue(models.Model):
    name     = models.CharField("Venue Name", max_length=120)
    address  = models.CharField(max_length=300)
    zip_code = models.CharField("Zip/Post Code", max_length=12)
    phone    = models.CharField('Contact Phone', max_length=20)
    web      = models.URLField('Web Address')
    email    = models.EmailField('Email Address')

    def __str__(self):
        return self.name


class Attendee(models.Model):
    fname = models.CharField('First Name', max_length=30)
    lname = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.fname + " " + self.lname


class Event(models.Model):
    name        = models.CharField('Event Name', max_length=120)
    date        = models.DateTimeField('Event Date')
#    venue       = models.CharField(max_length=120)
    venue       = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager     = models.CharField(max_length=60)
    attendee    = models.ManyToManyField(Attendee, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
