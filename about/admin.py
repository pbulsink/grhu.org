from django.contrib import admin
from about.models import About

class AboutAdmin(admin.ModelAdmin):
    fieldsets = [
        ('About', {'fields': ['about_type', 'name', 'email', 'byline',
                              'content']}),
        ('Photo', {'fields': ['image', 'tooltip']}),
        ('Other', {'fields': ['description', 'public'],
            'classes': ['collapse']})
    ]

admin.site.register(About, AboutAdmin)

