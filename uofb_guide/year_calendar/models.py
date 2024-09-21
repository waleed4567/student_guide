from django.db import models
from django.db.utils import OperationalError
from django.utils.translation import gettext_lazy as _
from college.models import College

class EventType(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    college = models.ForeignKey('college.College', verbose_name=_("College"), on_delete=models.SET_NULL, null=True)
    title = models.CharField(_("Title"), max_length=50) # Event Title # Example : Start of the Academic Year
    description = models.TextField(_("Description")) # Event Description # Short description of the event
    date = models.DateTimeField(_("Event Date"), auto_now=False, auto_now_add=False) # Event Date
    added_at = models.DateTimeField(_("Added At"), auto_now_add=True) # Event Added At
    event_type = models.ForeignKey('year_calendar.EventType', verbose_name=_("Event Type"), on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title
    