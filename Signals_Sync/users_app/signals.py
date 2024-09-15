import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print(f"Signal received for User: {instance.username}")
    time.sleep(5)
    print(f"Signal processing completed for User: {instance.username}")
