from django.apps import AppConfig



class NomadCoffeeNarynAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Nomad_Coffee_Naryn_app'

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa