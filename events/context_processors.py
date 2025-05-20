# events/context_processors.py
from .models import Event

def events_processor(request):
    return {
        'events': Event.objects.all()
    }