from django.shortcuts import render
from django.contrib.auth.models import User
import datetime
from django.http import HttpResponse

def create_user_and_check_signal(request):
    print(f"Before signal: {datetime.datetime.now()}")
    user = User.objects.create(username='testuser3', password='testpass3')
    print(f"After signal: {datetime.datetime.now()}")
    return HttpResponse("User created and signal triggered. Check console for time differences.")
