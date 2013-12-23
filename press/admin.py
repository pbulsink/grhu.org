from django.contrib import admin
from press.models import Press

class PressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Press Content',  {'fields': ['title', 'byline', 'content']}),
        ('Author Info', {'fields': ['author', 'author_email']}),
        ('Image Content', {'fields': ['image', 'tooltip', 'caption']}),
        ('Publishing',  {'fields': ['pub_date', 'description', 'public'],
            'classes': ['collapse']}),
        ('Boilerplate', {'fields': ['news', 'append_boilerplate', 'about_boilerplate'],
            'classes': ['collapse']})
    ]

admin.site.register(Press, PressAdmin)
