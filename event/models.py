from django.db import models

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
    pub_date = models.DateField('Publication Date', auto_now_add = True)
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    date = models.DateField('event date')
    start = models.TimeField('event start time')
    end = models.TimeField('event end', blank=True, null=True)
    location_name = models.CharField(max_length=150)
    location_street_address = models.CharField(max_length=120, blank=True, null=True)
    location_city = models.CharField(max_length=75, blank=True, null=True)
    location_provence = models.CharField(choices=PROVENCES, default="ON", max_length=3, blank=True, null=True)
    location_maps_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to = 'events/%Y/%m', blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    description = models.CharField(max_length = 500)
    price = models.CharField(max_length = 150)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.title

    def startdatetime(self):
        return datetime(self.date, self.start)

    def enddatetime(self):
        return datetime(self.date, self.end)

    def datetime(date, time):
        pass

