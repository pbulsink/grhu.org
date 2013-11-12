from django.db import models

class News(models.Model):
    title = models.CharField(max_length = 500)
    author = models.CharField(max_length = 75)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'news/%Y/%m/%d', blank=True, null=True)
    tooltip = models.CharField(max_length = 100)
    press = models.ForeignKey('press.Press')
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title
