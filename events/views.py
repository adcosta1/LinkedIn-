from django.shortcuts import render
from django.views import View
from events.models import Events

class EventsView(View):
    def get(self,request):
        events = Events.objects.filter(category=request.user.category)
        