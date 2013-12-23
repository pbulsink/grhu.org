from django.contrib import admin
from event.models import Event

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Info', {'fields': ['title', 'content', 'byline', 'price']}),
        ('Time', {'fields': ['date', 'start', 'end']}),
        ('Location', {'fields': ['location_name', 'location_street_address',
                                 'location_city', 'location_provence',
                                 'location_maps_url']}),
        ('Image', {'fields': ['image', 'tooltip', 'promo_poster']}),
        ('Other', {'fields': ['description', 'public'], 'classes': ['collapse']})
    ]

admin.site.register(Event, EventAdmin)

