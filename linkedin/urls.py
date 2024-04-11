"""
URL configuration for linkedin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts.views import Login_view,Register_view,ConnectionsView,AddEducationView,AddProfessionalExperienceView,MyProfileUpdateView
from jobs.views import JobsView
from events.views import EventsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',EventsView.as_view(),name="HomeView"),
    path('login/',Login_view.as_view(),name="LoginView"),
    path('myprofile/<int:pk>/', MyProfileUpdateView.as_view(), name="MyProfileView"),
    path('register/',Register_view.as_view(),name="RegisterView"),
    path('events/',EventsView.as_view(),name="EventsView"),
    path('jobs/',JobsView.as_view(),name="JobsView"),
    path('connections/',ConnectionsView.as_view(),name="ConnectionsView"),
    path('addeducation/',AddEducationView.as_view(),name="AddEducationView"),
    path('addexperience/',AddProfessionalExperienceView.as_view(),name="AddExperienceView"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
