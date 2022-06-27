from apps.scraper.views import scrap
from django.urls import path


urlpatterns = [
    path('',scrap),
]
