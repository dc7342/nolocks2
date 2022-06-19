from rest_framework import serializers
from api.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for Location
    """

    image = serializers.ImageField(required=False)

    class Meta:
        model = Location
        fields = ['created', 'longitude', 'latitude', 'comment', 'image']
        extra_kwargs = {'created': {'read_only': True}}

