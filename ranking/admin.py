from django.contrib import admin

from django.contrib import admin
from .models import Film
from .models import Review

admin.site.register(Film)
admin.site.register(Review)