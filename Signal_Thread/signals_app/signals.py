import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DemoModel

@receiver(post_save, sender=DemoModel)
def post_save_handler(sender, instance, **kwargs):
    current_thread = threading.current_thread()
    print(f"Signal handler thread: {current_thread.name}")
