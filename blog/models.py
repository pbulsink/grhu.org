from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=75)
    author_email = models.EmailField()
    byline = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog/%Y/%m/%d', blank=True, null=True)
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title
