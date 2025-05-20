# events/views.py
from django.views.generic import ListView, DetailView
from .models import Event, Episode

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    pk_url_kwarg = 'event_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['episodes'] = self.object.episodes.all()
        return context

class EpisodeDetailView(DetailView):
    model = Episode
    template_name = 'events/episode_detail.html'
    context_object_name = 'episode'
    pk_url_kwarg = 'episode_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = self.object.participants.all()
        context['performances'] = self.object.special_performances.all()
        context['collaborators'] = self.object.collaborators.all()
        context['moments'] = self.object.moments.all()
        return context