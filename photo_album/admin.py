from django.contrib import admin
from photo_album.models import Album
from photo_album.models import Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Album Info', {'fields': ['atitle', 'abyline', 'acontent']}),
        ('Relational', {'fields': ['ablog', 'aevent', 'anews', 'apress',
                                   'aproject']}),
        ('Publishing', {'fields': ['apublic', 'adescription'],
            'classes': ['collapse']}),
    ]
    inlines = [PhotoInline]

admin.site.register(Album, AlbumAdmin)

