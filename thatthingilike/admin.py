from django.contrib import admin

from .models import Thing, Tag, Location

admin.site.register(Thing)
admin.site.register(Tag)    
admin.site.register(Location)