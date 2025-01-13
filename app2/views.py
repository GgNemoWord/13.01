from django.shortcuts import render
from .models import *
# Create your views here.
def main(request):
    event = Event.objects.all()
    attendee = Attendee.objects.all()
    return render(request, 'event/index.html', {'events': event, 'attendees': attendee})