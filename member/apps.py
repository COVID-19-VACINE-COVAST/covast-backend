from django.apps import AppConfig


class MemberConfig(AppConfig):
    name = 'member'

    def ready(self):
        from member import signals
