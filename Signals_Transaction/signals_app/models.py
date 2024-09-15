from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=MyModel)
def post_save_handler(sender, instance, **kwargs):
    print("Signal received! Instance ID:", instance.id)
