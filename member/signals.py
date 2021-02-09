from django.dispatch import receiver
from django.db.models.signals import post_save

from member.models.token import Token
from member.models.user import User


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
