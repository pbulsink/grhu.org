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
    description = models.CharField(max_length = 500, blank=True, null=True)
    price = models.CharField(max_length = 150)
    public = models.BooleanField('Post Publicly', default=True)

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
                    desc = (line[:497] + '...') if len(line) > 500 else line
                    self.description = desc

