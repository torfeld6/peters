from django.shortcuts import render

from peters.events.models import Event


def index(request):
    event_list = Event.objects.order_by('date')
    context = {'event_list': event_list}
    return render(request, 'events/index.html', context)
