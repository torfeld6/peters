from django.contrib import admin

from peters.events.models import Event


class EventAdmin(admin.ModelAdmin):
    ordering = ('-date',)


admin.site.register(Event, EventAdmin)
