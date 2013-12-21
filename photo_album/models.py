from django.db import models
from sorl.thumbnail import ImageField
import os
from grhuorg.settings import FORCE_AUTO_NOW
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('album', slugify(instance.title),
                        slugify(filename).replace('-','_'))

class Album(models.Model):
    atitle = models.CharField(max_length = 100)
    apub_date = models.DateTimeField('Publication Date')
    amod_date = models.DateTimeField('Last Modified')
    abyline = models.CharField(max_length = 150)
    adescription = models.CharField(max_length = 200, blank=True, null=True)
    aproject = models.ForeignKey('project.Project', related_name='albums', null=True, blank=True)
    ablog = models.ForeignKey('blog.Blog', related_name='albums', null=True, blank=True)
    anews = models.ForeignKey('news.News', related_name='albums', null=True, blank=True)
    aevent = models.ForeignKey('event.Event', related_name='albums', null=True, blank=True)
    apress = models.ForeignKey('press.Press', related_name='albums', null=True, blank=True)
    acontent = models.TextField()
    apublic = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.atitle

    def save(self):
        if FORCE_AUTO_NOW:
            if not self.id:
                self.pub_date = datetime.datetime.now()
            self.mod_date = datetime.datetime.now()
        return super(News, self).save()

    def clean(self):
        if self.description != "" or self.description != None:
            if not self.id:
                lines = self.content.splitlines()
                for line in lines:
                    if line != "" and line != None:
                        desc = (line[:197] + '...') if len(line) > 200 else line
                        self.description = desc
                        break

class Photo(models.Model):
    palbum = models.ForeignKey(Album)
    ptitle = models.CharField(max_length = 150)
    pcaption = models.CharField(max_length = 500)
    ptooltip = models.CharField(max_length = 100)
    pimage = models.ImageField(upload_to = "albums/%Y/%m")
    pimage_date = models.DateTimeField('Image Taken Date', null=True, blank=True)
    ppub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    pmod_date = models.DateTimeField('Last Modified', auto_now = True)

    def __unicode__(self):
        return self.ptitle

    def save(self):
        if FORCE_AUTO_NOW:
            if not self.id:
                self.pub_date = datetime.datetime.now()
            self.mod_date = datetime.datetime.now()
        return super(News, self).save()
