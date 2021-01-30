import binascii
import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from member.models.user import User


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40, primary_key=True, verbose_name=_('key'))
    user = models.OneToOneField(to=User, related_name='auth_token', on_delete=models.CASCADE, verbose_name=_('user'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        db_table = 'token'
        verbose_name = 'Token'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
