from django.db import models

class About(models.Model):
    about_type = models.CharField(max_length = 10)
    name = models.CharField(max_length = 75)
    email = models.EmailField()
    byline = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to = 'about')
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.name

