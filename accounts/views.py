from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic import CreateView,UpdateView
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from accounts.forms import CreateuserForm,CreateEducationForm,CreateProfessionalExperienceForm
from accounts.models import LinkedinUser,Education,ProfessionalExperience
from django.urls import reverse_lazy

class Login_view(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html',{})
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user != None:
            login(request,user)
            return redirect("EventsView")
        return render(request,'login.html',{})
        
        
class Register_view(View):
    def get(self, request):
        form = CreateuserForm() 
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateuserForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            user.photo = request.FILES['photo']
            user.save()
            return redirect('LoginView')

        return render(request, 'register.html', {'form': form})
        
        
        
class ConnectionsView(View):
    def get(self,request):
        user = get_object_or_404(LinkedinUser, username= request.user.username)
        users = LinkedinUser.objects.filter(state=user.state,category = user.category)
        return render(request, 'connections.html', {'users':users})
    
class AddEducationView(CreateView):
    form_class = CreateEducationForm
    template_name = 'education_form.html'
    success_url = reverse_lazy('EventsView')
    
    def form_valid(self, form):
       
        form.instance.userid = self.request.user.id
        user = get_object_or_404(User, pk=self.request.user.pk)
        education_instance = form.save(commit=False)  
        education_instance.save()  
        linkedin_user = get_object_or_404(LinkedinUser, user_ptr=user)  
        linkedin_user.education = education_instance 
        linkedin_user.save() 
        return super().form_valid(form)
    
class AddProfessionalExperienceView(CreateView):
    form_class = CreateProfessionalExperienceForm
    template_name = 'experience_form.html'
    success_url = reverse_lazy('EventsView')
    
    def form_valid(self, form):
       
        form.instance.userid = self.request.user.id
        user = get_object_or_404(User, pk=self.request.user.pk)
        professional_instance = form.save(commit=False) 
        professional_instance.save()  
        linkedin_user = get_object_or_404(LinkedinUser, user_ptr=user)  
        linkedin_user.experience = professional_instance  
        linkedin_user.save()  
        return super().form_valid(form)

class MyProfileUpdateView(UpdateView):
    template_name = "myprofile.html"
    form_class = CreateuserForm  
    model = LinkedinUser
    success_url = reverse_lazy("EventsView")
