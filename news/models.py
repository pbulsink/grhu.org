from django.db import models
from sorl.thumbnail import ImageField
import datetime
import os
from grhuorg.settings import FORCE_AUTO_NOW
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('news', str(datetime.date.today().year),
                        str(datetime.date.today().month),
                        slugify(filename).replace('-','_'))

class News(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Publication Date', blank=True, null=True)
    mod_date = models.DateTimeField('Last Modified', blank=True, null=True)
    author = models.CharField(max_length=75)
    author_email = models.EmailField()
    byline = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to = get_image_path, blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    caption = models.CharField(max_length = 250, blank=True, null=True)
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
    
    def mod_diff_day(self):
        if (self.pub_date.date == self.mod_date.date):
            return True
        return False

    def save(self):
        if FORCE_AUTO_NOW:
            if not self.id:
                self.pub_date = datetime.datetime.now()
            self.mod_date = datetime.datetime.now()
        else:
            self.mod_date = self.pub_date
        return super(News, self).save()

    def get_absolute_url(self):
        return "/news/%i/" % self.id