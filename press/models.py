from django.db import models
from about.models import About

class Press(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    mod_date = models.DateTimeField('Last Modified', auto_now = True)
    author = models.CharField(max_length=75)
    author_email = models.EmailField()
    byline = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to = 'blog/%Y/%m/%d', blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True)
    caption = models.CharField(max_length = 250, blank=True, null=True)
    description = models.CharField(max_length = 500, blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)
    news = models.ForeignKey('news.News', related_name='press_release', null=True, blank=True)
    append_boilerplate = models.BooleanField('Add Boilerplate?', default=True)
    about_boilerplate = models.ForeignKey('about.About', related_name='boiler_plate')

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.description != "" or self.description != None:
            lines = self.content.splitlines()
            for line in lines:
                if line != "" and line != None:
                    desc = (line[:497] + '...') if len(line) > 500 else line
                    self.description = desc

    def full_content(self):
        if self.append_boilerplate:
            true_str = self.content
            boiler = About.objects.filter(about_type="Boilerplate")
            true_str.join("/n")
            true_str.join(boiler)
            return true_str
        else:
            return self.content
