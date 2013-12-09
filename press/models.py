from django.db import models
from sorl.thumbnail import ImageField
import datetime
import os
from grhuorg.settings import FORCE_AUTO_NOW
from about.models import About
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('press', datetime.date.today().year,
                        datetime.date.today().month,
                        slugify(filename).replace('-','_'))

class Press(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Publication Date')
    mod_date = models.DateTimeField('Last Modified')
    author = models.CharField(max_length=75)
    author_email = models.EmailField()
    byline = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to = get_image_path, blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    caption = models.CharField(max_length = 250, blank=True, null=True)
    description = models.CharField(max_length = 200, blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)
    news = models.ForeignKey('news.News', related_name='press_release', null=True, blank=True)
    append_boilerplate = models.BooleanField('Add Boilerplate?', default=True)
    about_boilerplate = models.ForeignKey('about.About', related_name='boiler_plate', blank=True, null=True)

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.description != "" or self.description != None:
            lines = self.content.splitlines()
            for line in lines:
                if line != "" and line != None:
                    desc = (line[:197] + '...') if len(line) > 200 else line
                    self.description = desc
                    break

    def full_content(self):
        if self.append_boilerplate:
            true_str = self.content
            boiler = About.objects.filter(about_type="Boilerplate")
            true_str.join("/n")
            true_str.join(boiler)
            return true_str
        else:
            return self.content

    def mod_diff_day(self):
        if (self.pub_date.date == self.mod_date.date):
            return True
        return False

    def save(self):
        if FORCE_AUTO_NOW:
            if not self.id:
                self.pub_date = datetime.datetime.now()
            self.mod_date = datetime.datetime.now()
        return super(News, self).save()
