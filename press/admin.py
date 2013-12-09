from django.contrib import admin
from press.models import Press

class PressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Press Content',  {'fields': ['title', 'byline', 'content', 'description']}),
        ('Author Info', {'fields': ['author', 'author_email']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publish Time',  {'fields': ['pub_date', 'mod_date', 'public']}),
        ('Relational:', {'fields': ['news', 'append_boilerplate', 'about_boilerplate']})
    ]

admin.site.register(Press, PressAdmin)
