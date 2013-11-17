from django.db import models

class Project(models.Model):
    pub_date = models.DateTimeField('Publication Date', auto_now_add = True)
    mod_date = models.DateTimeField('Last Modified', auto_now = True)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    byline = models.CharField(max_length = 150)
    image = models.ImageField(upload_to = 'projects/%Y', blank=True, null=True)
    caption = models.CharField(max_length = 250, blank=True, null=True)
    tooltip = models.CharField(max_length = 100, blank=True, null=True) 
    active = models.BooleanField(default=True)
    description = models.CharField(max_length = 500, blank=True, null=True)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.title

    def clean(self):
        if self.description != "" or self.description != None:
            lines = self.content.splitlines()
            for line in lines:
                if line != "" and line != None:
                    desc = (line[:497] + '...') if len(line) > 500 else line
                    self.description = desc
