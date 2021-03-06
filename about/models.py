from django.db import models
from sorl.thumbnail import ImageField
from grhuorg.settings import FORCE_AUTO_NOW
from django.utils.text import slugify
import os
import datetime

def get_image_path(instance, filename):
    filename = os.path.basename(filename)
    return os.path.join('about', str(datetime.date.today().year),
                        slugify(filename).replace('-','_'))

class About(models.Model):
    GENERAL = "General"
    DIRECTOR = "Director"
    BOARD = "Board"
    AGENT = "Agent"
    BOILERPLATE = "Boilerplate"
    ABOUT_TYPE = (
        (GENERAL, 'General'),
        (DIRECTOR, 'Director'),
        (AGENT, 'Agent'),
        (BOARD, 'Board'),
        (BOILERPLATE, 'Boilerplate')
    )
    about_type = models.CharField(choices=ABOUT_TYPE, max_length=12)
    name = models.CharField(max_length = 75)
    email = models.EmailField()
    byline = models.CharField(max_length = 250)
    content = models.TextField()
    image = models.ImageField(upload_to = get_image_path, blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    description = models.CharField(max_length = 200,
                                   default='Leave unchanged to auto-generage description',
                                   blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)
    pub_date = models.DateTimeField('Added Date', auto_now_add=True, auto_now=True)

    def clean(self):
        if self.description != "" or self.description != None:
            if not self.id:
                lines = self.content.splitlines()
                for line in lines:
                    if line != "" and line != None: #strips leading blanklines
                        desc = (line[:197] + '...') if len(line) > 200 else line
                        self.description = desc
                        break

    def __unicode__(self):
        return self.name

    def first_name(self):
        return self.name.split(' ', 1)[0]

    def get_boilerplate(self):
        return About.objects.get(about_type="Boilerplate")

    def get_absolute_url(self):
        return "/about/%i/" % self.id