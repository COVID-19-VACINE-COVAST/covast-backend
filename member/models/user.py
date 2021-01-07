import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uuid'))
    last_name = None
    first_name = None

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) username is {self.username}'
