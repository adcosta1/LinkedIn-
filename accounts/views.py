from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login

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
