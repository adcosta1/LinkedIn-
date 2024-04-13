from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from events.models import Events
from accounts.models import LinkedinUser
from events.forms import CreateEventForm

class EventsView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get(self,request):
        user = get_object_or_404(LinkedinUser, username=request.user.username )

        search = Q(Q(category=user.category) | Q(organizer__state=user.state))
        events = Events.objects.filter(search)
        form = CreateEventForm()
        return render(request, 'event.html',{'events':events, 'form':form})
    
    def post(self,request):
        form = CreateEventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            event.organizer = LinkedinUser.objects.get(username=request.user.username)
            event.save()
            
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        search = Q(Q(category=user.category) | Q(organizer__state=user.state))
        events = Events.objects.filter(search)
        form = CreateEventForm()
        return render(request, 'event.html',{'events':events, 'form':form})



    
class DeleteEventView(View):
    def post(self, request, *args, **kwargs):
        event_id = kwargs['pk']
        event = Events.objects.get(pk=event_id)
        event.delete()
        return redirect('EventsView') 