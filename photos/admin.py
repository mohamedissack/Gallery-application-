from django.contrib import admin
from .models import Image, Location, Catergory

# Register your model.
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Catergory)