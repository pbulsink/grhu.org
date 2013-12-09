from django.db import models
from sorl.thumbnail import ImageField
from grhuorg.settings import FORCE_AUTO_NOW
from django.utils.text import slugify

def get_image_path(instance, filename):
    return os.path.join('about', datetime.date.today().year,
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
    image = models.ImageField(upload_to = get_image_path)
    tooltip = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    public = models.BooleanField('Post Publicly', default=True)

    def __unicode__(self):
        return self.name

    def first_name(self):
        return self.name.split(' ', 1)[0]

