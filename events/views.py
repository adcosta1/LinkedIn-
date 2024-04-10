from django.shortcuts import render,get_object_or_404
from django.views import View
from events.models import Events
from accounts.models import LinkedinUser
from events.forms import CreateEventForm

class EventsView(View):
    def get(self,request):
        user = get_object_or_404(LinkedinUser, username=request.user.username )
        print(user)
        events = Events.objects.filter(category=user.category)
        form = CreateEventForm()
        return render(request, 'event.html',{'events':events, 'form':form})
    
    def post(self,request):
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            event.organizer = LinkedinUser.objects.get(username=request.user.username)
            event.save()
            
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        events = Events.objects.filter(category=user.category)
        form = CreateEventForm()
        return render(request, 'event.html',{'events':events, 'form':form})
