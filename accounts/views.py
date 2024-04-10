from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login
from accounts.forms import CreateuserForm

class Login_view(View):
    def get(self,request):
        return render(request,'login.html',{})
    
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user != None:
            login(request,user)
            return redirect("events")
        
        
class Register_view(View):
    def get(self, request):
        form = CreateuserForm() 
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CreateuserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('LoginView')

        return render(request, 'register.html', {'form': form})
        
        
        
