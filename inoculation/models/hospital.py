import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBaseModel


class Hospital(AbstractBaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    address = models.CharField(max_length=300, verbose_name=_('address'))
    road_address = models.CharField(max_length=300, verbose_name=_('road_address'))
    contact = models.CharField(max_length=13, verbose_name=_('contact'))
    place_url = models.URLField(max_length=500, verbose_name=_('place_url'))
    start_business_hours = models.DateTimeField(null=True, blank=True, verbose_name=_('start_business_hours'))
    end_business_hours = models.DateTimeField(null=True, blank=True, verbose_name=_('end_business_hours'))
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))

    class Meta:
        db_table = 'hospital'
        verbose_name = 'Hospital'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))
        unique_together = ('latitude', 'longitude', )

    def __str__(self):
        return f'ID({self.id}) name is {self.name}'
