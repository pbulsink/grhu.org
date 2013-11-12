from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    event_date = models.DateTimeField('event date')
    event_location = models.CharField(max_length=300)
    image = models.ImageField(upload_to = '/static/events/%Y/%m', blank=True, null=True)
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title

