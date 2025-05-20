from django.db import models
from django.urls import reverse

class Event(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'event_id': self.pk})

class Episode(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='episodes')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='episodes/')
    
    def __str__(self):
        return f"{self.name} - {self.title}"
    
    def get_absolute_url(self):
        return reverse('episode_detail', kwargs={'episode_id': self.pk})

class Participant(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='participants')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='participants/')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SpecialPerformance(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='special_performances')
    image = models.ImageField(upload_to='performances/')
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Collaborator(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='collaborators')
    image = models.ImageField(upload_to='collaborators/')
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class Moment(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE, related_name='moments')
    image = models.ImageField(upload_to='moments/')
    
    def __str__(self):
        return f"Moment from {self.episode.name}"