from django.db import models
from sorl.thumbnail import ImageField
import datetime
import os
from grhuorg.settings import FORCE_AUTO_NOW
from grhuorg.formatChecker import ContentTypeRestrictedFileField
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('events', slugify(instance.title),
                        slugify(filename).replace('-','_'))
    
class Event(models.Model):
    PROVENCES = (
        ('ON', 'Ontario'),
        ('AB', 'Alberta'),
        ('BC', 'British Columbia'),
        ('SK', 'Saskatchewan'),
        ('MB', 'Manitoba'),
        ('NB', 'New Brunswick'),
        ('NS', 'Nova Scotia'),
        ('QC', 'Quebec'),
        ('PEI', 'Prince Edward Island'),
        ('NL', 'Newfoundland'),
        ('YK', 'Yukon'),
        ('NWT', 'Northwest Territories'),
        ('NU', 'Nunavut'),
    )
    title = models.CharField(max_length=100)
    pub_date = models.DateField('Publication Date')
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    date = models.DateField('Event Date')
    start = models.TimeField('Event Start Time')
    end = models.TimeField('Event End', blank=True, null=True)
    location_name = models.CharField('Event Location Name', max_length=150)
    location_street_address = models.CharField('Location Street Address',
                                               max_length=120, blank=True,
                                               null=True)
    location_city = models.CharField('Location City', max_length=75, blank=True,
                                     null=True)
    location_provence = models.CharField('Location Province', choices=PROVENCES,
                                         default="ON", max_length=3, blank=True,
                                         null=True)
    location_maps_url = models.URLField("Location's Google Maps Url",
                                        blank=True, null=True)
    image = models.ImageField(upload_to = get_image_path)
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    price = models.CharField('Price', max_length = 150)
    public = models.BooleanField('Post Publicly', default=True)
    promo_poster = ContentTypeRestrictedFileField(
        upload_to=get_image_path,
        content_types=[
            'application/pdf',
            'application/zip',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'application/vnd.ms-powerpoint',
            'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            'image/jpeg',
            'image/gif',
            'image/png',
            ],
        max_upload_size=10485760
    )

    def __unicode__(self):
        return self.title

    def startdatetime(self):
        return datetime(self.date, self.start)

    def enddatetime(self):
        return datetime(self.date, self.end)

    def datetime(datein, timein):
        """returns a ISOdatetime to the requester for itemprop in template"""
        datefrmt = datein.strftime('%Y-%m-%d')
        timefrmt = timein.strftime('T%H:%M%z')
        datetimefrmt = datefrmt + timefrmt
        return datetimefrmt

    def clean(self):
        if self.description != "" or self.description != None:
            lines = self.content.splitlines()
            for line in lines:
                if line != "" and line != None:
                    desc = (line[:197] + '...') if len(line) > 200 else line
                    self.description = desc
                    break

    def save(self):
        if FORCE_AUTO_NOW:
            if not self.id:
                self.pub_date = datetime.datetime.now()
            self.mod_date = datetime.datetime.now()
        return super(News, self).save()
