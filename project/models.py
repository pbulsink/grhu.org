from django.db import models
from sorl.thumbnail import ImageField
import datetime
from grhuorg.settings import FORCE_AUTO_NOW
from django.utils.text import slugify
import os

def get_image_path(instance, filename):
    return os.path.join('project', datetime.date.today().year,
                        slugify(instance.title).replace('-','_'),
                        slugify(filename).replace('-','_'))

class Project(models.Model):
    pub_date = models.DateTimeField('Publication Date')
    start_date = models.DateTimeField('Project Start Date')
    end_date = models.DateTimeField('Project End Date')
    title = models.CharField('Project Title', max_length = 100)
    short_query = models.CharField('Project Short Query for Code', max_length = 15)
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = get_image_path, blank=True, null=True)
    caption = models.CharField(max_length = 250, blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True) 
    active = models.BooleanField('Currently active project?', default=True)
    description = models.CharField(max_length = 200, blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.title

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
        return super(News, self).save()
