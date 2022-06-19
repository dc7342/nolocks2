from django.contrib import admin
from api.models import Location


class LocationAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = (
        'id',
        'longitude',
        'latitude',
        'comment',
    )


admin.site.register(Location, LocationAdmin)
