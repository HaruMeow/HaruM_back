from django.contrib import admin
from cal.models import CalendarEvent
from cal.models import targetEvent

# Register your models here.
admin.site.register(CalendarEvent)
admin.site.register(targetEvent)
