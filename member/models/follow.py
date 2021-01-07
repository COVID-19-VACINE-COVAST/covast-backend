from django.db import models
from django.utils.translation import ugettext_lazy as _

from member.models.user import User


class Follow(models.Model):
    follow_user = models.ForeignKey(to=User, related_name='follow_user', on_delete=models.CASCADE,
                                    verbose_name=_('follow_user'))
    follower_user = models.ForeignKey(to=User, related_name='follower_user', on_delete=models.CASCADE,
                                      verbose_name=_('follower_user'))

    class Meta:
        db_table = 'follow'
        verbose_name = 'Follow'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) {self.follower_user.username} is following {self.follow_user.username}'
