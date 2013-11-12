from django.db import models

class Press(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'press/%Y/%m/%d', blank=True, null=True)
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title


