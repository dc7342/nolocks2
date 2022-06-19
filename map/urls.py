from django.urls import path
from map.views import web_map

urlpatterns = [
    path('', web_map)
]
