import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from member.models.user import User

from utils.models import AbstractBaseModel


class Review(AbstractBaseModel):
    user = models.ForeignKey(to=User, related_name='review', on_delete=models.CASCADE, verbose_name=_('user'))
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    vaccine_kind = models.CharField(max_length=30, verbose_name=_('vaccine_kind'))
    contents = models.CharField(max_length=1000, verbose_name=_('contents'))
    like = models.PositiveIntegerField(default=0, verbose_name=_('like'))
    unlike = models.PositiveIntegerField(default=0, verbose_name=_('unlike'))

    class Meta:
        db_table = 'review'
        verbose_name = 'Review'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) author is {self.user.username}'
