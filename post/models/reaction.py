from django.db import models
from django.utils.translation import ugettext_lazy as _

from member.models.user import User

from post.models.comment import Comment
from post.models.review import Review

from utils.models import AbstractBaseModel


class Reaction(AbstractBaseModel):
    REACTION_KIND_CHOICES = (
        (0, 'unlike'),
        (1, 'like'),
    )

    user = models.ForeignKey(to=User, related_name='reactions', on_delete=models.CASCADE, verbose_name=_('user'))
    review = models.OneToOneField(to=Review, null=True, blank=True, related_name='review', on_delete=models.CASCADE,
                                  verbose_name=_('review'))
    comment = models.OneToOneField(to=Comment, null=True, blank=True, related_name='comment', on_delete=models.CASCADE,
                                   verbose_name=_('comment'))
    kind = models.IntegerField(choices=REACTION_KIND_CHOICES, null=True, blank=True, verbose_name=_('kind'))

    class Meta:
        db_table = 'reaction'
        verbose_name = 'Reaction'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) reaction from {self.user.username}'
