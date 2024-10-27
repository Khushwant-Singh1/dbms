from django.contrib import admin
from .models import Listing, Photo, Amenity
# Register your models here.

admin.site.register(Listing)
admin.site.register(Photo)
admin.site.register(Amenity)