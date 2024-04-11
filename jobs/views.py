from django.shortcuts import render, get_object_or_404
from django.views import View
from jobs.models import Job
from jobs.forms import PublishJobForm
from accounts.models import LinkedinUser
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class JobsView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get(self,request):
          
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        job = Job.objects.filter(category=user.category)
        form = PublishJobForm()
        return render(request, 'jobs.html',{'jobs':job, 'form':form})
    
    def post(self,request):
        form = PublishJobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()
            job.postedby = get_object_or_404(LinkedinUser, username= request.user.username)
            job.save()
            
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        job = Job.objects.filter(category=user.category, state= user.state)
        form = PublishJobForm()
        return render(request, 'jobs.html',{'jobs':job, 'form':form})