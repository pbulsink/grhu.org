from django.db import models
from sorl.thumbnail import ImageField
import datetime
import os
from grhuorg.settings import FORCE_AUTO_NOW
from lib.formatChecker import ContentTypeRestrictedFileField
from django.utils.text import slugify
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], ["^lib\.formatChecker\.ContentTypeRestrictedFileField"])

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
    pub_date = models.DateField('Publication Date', blank=True, null=True)
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    date = models.DateField('Event Date')
    start = models.TimeField('Event Start Time', blank=True, null=True)
    end = models.TimeField('Event End', blank=True, null=True)
    location_name = models.CharField('Event Location Name', max_length=150,
                                     blank=True, null=True)
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
    image = models.ImageField('Article Image', upload_to = get_image_path,
                              blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    description = models.CharField(max_length = 200, blank=True, null=True)
    price = models.CharField('Price', max_length = 150, blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)
    promo_poster = ContentTypeRestrictedFileField(
        'Promotional Poster',
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
        max_upload_size=10485760,
        blank=True,
        null=True,
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
            if not self.id:
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
        else:
            self.mod_date = self.pub_date
        return super(Event, self).save()

    def get_absolute_url(self):
        return "/event/%i/" % self.id