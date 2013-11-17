from django.db import models

class About(models.Model):
    GENERAL = "General"
    DIRECTOR = "Director"
    BOARD = "Board"
    AGENT = "Agent"
    ABOUT_TYPE = (
        (GENERAL, 'General'),
        (DIRECTOR, 'Director'),
        (AGENT, 'Agent'),
        (BOARD, 'Board')
    )
    about_type = models.CharField(choices=ABOUT_TYPE, max_length=10)
    name = models.CharField(max_length = 75)
    email = models.EmailField()
    byline = models.CharField(max_length = 250)
    content = models.TextField()
    image = models.ImageField(upload_to = 'about')
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.name

    def first_name(self):
        return self.name.split(' ', 1)[0]

