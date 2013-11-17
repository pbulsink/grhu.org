from django.db import models


class Album(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    mod_date = models.DateTimeField('Last Modified', auto_now = True)
    byline = models.CharField(max_length = 150)
    description = models.CharField(max_length = 500)
    project = models.ForeignKey('project.Project', related_name='albums', null=True, blank=True)
    blog = models.ForeignKey('blog.Blog', related_name='albums', null=True, blank=True)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length = 150)
    caption = models.CharField(max_length = 500)
    image = models.ImageField(upload_to = "albums/%Y/%m")
    image_date = models.DateTimeField('Image Taken Date', null=True, blank=True)
    pub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    mod_date = models.DateTimeField('Last Modified', auto_now = True)

    def __unicode__(self):
        return self.title
