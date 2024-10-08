from django.apps import AppConfig

class AnchorConfig(AppConfig):
    name = 'anchor'

    def ready(self):
        from polaris.integrations import register_integrations
        from .sep1 import return_toml_contents
        # from .sep24.deposit import AnchorDeposit
        # from .sep24.withdraw import AnchorWithdraw

        register_integrations(
            toml=return_toml_contents,
            # deposit=AnchorDeposit(),
            # withdraw=AnchorWithdraw()
        )