from django.contrib import admin
from apps.scraper.models import Keyword, Url

# Register your models here.

admin.site.register(Url)
admin.site.register(Keyword)