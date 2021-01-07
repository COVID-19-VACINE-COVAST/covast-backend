import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBaseModel


class Vaccine(AbstractBaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    name = models.CharField(max_length=50, verbose_name=_('name'))
    development_country = models.CharField(max_length=30, verbose_name=_('development_country'))
    development_company = models.CharField(max_length=30, verbose_name=_('development_company'))
    release_date = models.DateField(verbose_name=_('release_date'))
    kind = models.CharField(max_length=30, verbose_name=_('kind'))
    clinical_trial_stage = models.PositiveIntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])

    class Meta:
        db_table = 'vaccine'
        verbose_name = 'Vaccine'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) name is {self.name} kind is {self.kind}'


