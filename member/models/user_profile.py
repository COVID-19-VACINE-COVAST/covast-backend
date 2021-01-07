import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from member.models.user import User

from utils.models import AbstractBaseModel


class UserProfile(AbstractBaseModel):
    SEX_CHOICES = (
        (0, 'man'),
        (1, 'woman'),
    )

    user = models.OneToOneField(to=User, related_name='user_profile', on_delete=models.CASCADE, verbose_name=_('user'))
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uuid'))
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    birth = models.DateField()
    sex = models.PositiveIntegerField(choices=SEX_CHOICES, validators=[MaxValueValidator(1), MinValueValidator(0)])
    followers_num = models.PositiveIntegerField(default=0)
    inoculation_at = models.DateTimeField()

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'UserProfile'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) full_name is {self.last_name} {self.first_name}'
