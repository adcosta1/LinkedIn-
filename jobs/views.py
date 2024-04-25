from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from django.views.generic import DeleteView
from jobs.models import Job
from jobs.forms import PublishJobForm
from accounts.models import LinkedinUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy

# Create your views here.
class JobsView(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
    def get(self,request):
          
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        search = Q(Q(category=user.category) and Q(state=user.state))
        jobs = Job.objects.filter(search)

        form = PublishJobForm()
        return render(request, 'jobs.html',{'jobs':jobs, 'form':form})
    
    def post(self,request):
        form = PublishJobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save()
            job.postedby = get_object_or_404(LinkedinUser, username= request.user.username)
            job.save()
        
        user = get_object_or_404(LinkedinUser, username= request.user.username )
        search = Q(Q(category=user.category))
        jobs = Job.objects.filter(search)
        jobs = reversed(jobs)
        form = PublishJobForm()
        return render(request, 'jobs.html',{'jobs':jobs, 'form':form})
    
class DeleteJobView(View):
    def post(self, request, *args, **kwargs):
        job_id = kwargs['pk']
        job = Job.objects.get(pk=job_id)
        job.delete()
        return redirect('JobsView') 