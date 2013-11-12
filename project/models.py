from django.db import models

class Project(models.Model):
    pub_date = models.DateTimeField('date added')
    title = models.CharField(max_length = 200)
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'projects/%Y', blank=True, null=True)
    tooltip = models.CharField(max_length = 100) 
    active = models.BooleanField()
    description = models.CharField(max_length = 500)

    def __unicode__(self):
        return self.title

