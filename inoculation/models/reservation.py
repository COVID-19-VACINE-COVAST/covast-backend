import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from inoculation.models.hospital import Hospital
from inoculation.models.vaccine import Vaccine

from member.models.user import User

from utils.models import AbstractBaseModel


class Reservation(AbstractBaseModel):
    user = models.OneToOneField(to=User, related_name='reservation', on_delete=models.CASCADE, verbose_name=_('user'))
    hospital = models.ForeignKey(to=Hospital, related_name='hospital_reservations', on_delete=models.CASCADE,
                                 verbose_name=_('hospital'))
    vaccine = models.ForeignKey(to=Vaccine, related_name='hospital_reservations', on_delete=models.CASCADE,
                                verbose_name=_('vaccine'))
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    reservation_time = models.DateTimeField()

    class Meta:
        db_table = 'reservation'
        verbose_name = 'Reservation'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) user is {self.user.username} inoculation in hospital {self.hospital.name} vaccine ' \
            f'vaccine {self.vaccine.name}'
