from django.db import models

class Album(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 75)
    pub_date = models.DateTimeField('Date Published')
    byline = models.CharField(max_length = 150)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length = 150)
    caption = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = "albums/%Y/%m")
    image_date = models.DateTimeField('Image Taken Date')

    def __unicode__(self):
        return self.title
