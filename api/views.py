from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from api.models import Location
from api.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    Using ViewSet from Django Rest Framework.
    Implements all the behaviour through serialization of the requests.
    """

    # TODO: Add bot auth
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = Location.objects.all().order_by('created')
    parser_classes = (MultiPartParser, FormParser)
    # Serializer
    serializer_class = LocationSerializer
