from django.core.management.base import BaseCommand
from myapp.models import MyModel
from django.db import transaction

class Command(BaseCommand):
    help = "Test signal running in the same transaction as the caller"

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                self.stdout.write("Creating a MyModel instance")
                obj = MyModel.objects.create(name="Test Instance")

                self.stdout.write("Raising exception to trigger rollback")
                raise Exception("Simulating an error")
        except Exception as e:
            self.stdout.write(f"Transaction rolled back due to: {e}")

        exists = MyModel.objects.filter(name="Test Instance").exists()
        self.stdout.write(f"Check if the object exists: {exists}")
