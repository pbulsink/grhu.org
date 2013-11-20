from django.db import models


class Album(models.Model):
    atitle = models.CharField(max_length = 200)
    apub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    amod_date = models.DateTimeField('Last Modified', auto_now = True)
    abyline = models.CharField(max_length = 150)
    adescription = models.CharField(max_length = 500)
    aproject = models.ForeignKey('project.Project', related_name='albums', null=True, blank=True)
    ablog = models.ForeignKey('blog.Blog', related_name='albums', null=True, blank=True)
    acontent = models.TextField()
    apublic = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.atitle

class Photo(models.Model):
    palbum = models.ForeignKey(Album)
    ptitle = models.CharField(max_length = 150)
    pcaption = models.CharField(max_length = 500)
    pimage = models.ImageField(upload_to = "albums/%Y/%m")
    pimage_date = models.DateTimeField('Image Taken Date', null=True, blank=True)
    ppub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    pmod_date = models.DateTimeField('Last Modified', auto_now = True)

    def __unicode__(self):
        return self.ptitle
