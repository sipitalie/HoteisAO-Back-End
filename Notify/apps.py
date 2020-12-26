from django.apps import AppConfig


class NotifyConfig(AppConfig):
    name = 'Notify'

    def ready(self):
        import Notify.signals  # noqa
