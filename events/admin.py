from django.contrib import admin
from .models import Event, Episode, Participant, SpecialPerformance, Collaborator, Moment

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1
    show_change_link = True

class ParticipantInline(admin.TabularInline):
    model = Participant
    extra = 1

class SpecialPerformanceInline(admin.TabularInline):
    model = SpecialPerformance
    extra = 1

class CollaboratorInline(admin.TabularInline):
    model = Collaborator
    extra = 1

class MomentInline(admin.TabularInline):
    model = Moment
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [EpisodeInline]

@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'event')
    list_filter = ('event',)
    search_fields = ('name', 'title', 'description')
    inlines = [ParticipantInline, SpecialPerformanceInline, CollaboratorInline, MomentInline]

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'designation', 'company', 'episode')
    list_filter = ('episode__event', 'episode')
    search_fields = ('first_name', 'last_name', 'designation', 'company')

@admin.register(SpecialPerformance)
class SpecialPerformanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode')
    list_filter = ('episode__event', 'episode')
    search_fields = ('title',)

@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode')
    list_filter = ('episode__event', 'episode')
    search_fields = ('title',)

@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ('episode',)
    list_filter = ('episode__event', 'episode')