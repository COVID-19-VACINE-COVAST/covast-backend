import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _

from member.models.user import User

from post.models.review import Review

from utils.models import AbstractBaseModel


class Comment(AbstractBaseModel):
    user = models.ForeignKey(to=User, related_name='comments', on_delete=models.CASCADE, verbose_name=_('user'))
    review = models.ForeignKey(to=Review, related_name='reviews', on_delete=models.CASCADE, verbose_name=_('review'))
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))
    contents = models.CharField(max_length=1000)
    like = models.PositiveIntegerField(verbose_name=_('like'))
    unlike = models.PositiveIntegerField(verbose_name=_('unlike'))
    deleted_at = models.DateField(null=True, blank=True, verbose_name=_('deleted_at'))

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) author is {self.user.username} about review {self.review.id}'
