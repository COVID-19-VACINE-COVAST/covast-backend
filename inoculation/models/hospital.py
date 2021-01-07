import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBaseModel


class Hospital(AbstractBaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    address = models.CharField(max_length=300, verbose_name=_('adderss'))
    contact = models.CharField(max_length=13)
    start_business_hours = models.DateTimeField()
    end_business_hours = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = 'hospital'
        verbose_name = 'Hospital'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) name is {self.name}'
