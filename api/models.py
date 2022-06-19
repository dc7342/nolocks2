from django.db import models
from django.utils import timezone


# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Location(models.Model):
    """
    The one and only model in the project, describes a point with coordinates.
    """
    created = models.DateTimeField(verbose_name='Дата и время добавления', null=False, blank=False)
    longitude = models.CharField(verbose_name='Долгота', null=True, blank=True, max_length=16)
    latitude = models.CharField(verbose_name='Широта', null=True, blank=True, max_length=16)
    comment = models.CharField(max_length=256, verbose_name='Комментарий к точке', null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return f'{self.longitude} {self.latitude}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        """
        Auto set datetime
        """
        self.created = timezone.now()
        return super().save()
