from django.contrib import admin

from .models import Artist, Albom, Songs

admin.site.register([Artist, Albom, Songs])