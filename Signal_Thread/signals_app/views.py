import threading
from django.shortcuts import HttpResponse
from .models import DemoModel

def create_model_instance(request):
    current_thread = threading.current_thread()
    print(f"Caller thread: {current_thread.name}")
    instance = DemoModel.objects.create(name="Test Instance")
    return HttpResponse(f"Created DemoModel instance with ID: {instance.id}")
