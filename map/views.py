from django.shortcuts import render
from api.models import Location
from nolocks2.settings import MEDIA_URL


def web_map(request):
    """
    Rendering of the web map with openmap.
    """
    points = Location.objects.all()
    return render(request, 'index.html', context={'points': points, 'MEDIA_URL': MEDIA_URL})
