# events/urls.py
from django.urls import path
from .views import EventListView, EventDetailView, EpisodeDetailView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('events/<int:event_id>/', EventDetailView.as_view(), name='event_detail'),
    path('episodes/<int:episode_id>/', EpisodeDetailView.as_view(), name='episode_detail'),
]