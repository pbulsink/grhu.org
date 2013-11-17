from django.db import models

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
    description = models.CharField(max_length = 500)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.title
