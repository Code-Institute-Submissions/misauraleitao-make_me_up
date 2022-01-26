from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        '''Overriding the ready method and 
        importing our signals module.'''
        import checkout.signals
