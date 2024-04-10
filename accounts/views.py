from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login
from accounts.forms import CreateuserForm
from accounts.models import LinkedinUser

class Login_view(View):
    def get(self,request):
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
        connections = LinkedinUser.objects.filter(state=user.state,category = user.category)
        return render(request, 'connections.html', {'connections':connections})