from django.contrib import admin
from accounts.models import LinkedinUser,Education,ProfessionalExperience
from jobs.models import Job
from events.models import Events

class LinkedinUserAdmin(admin.ModelAdmin):
    
    list_display = ('username',)
    search_fields = ('username',)
    
class EducationAdmin(admin.ModelAdmin):
    
    list_display = ('degreename','userid')
    search_fields = ('degreename','userid')
    
class ProfessionalExperienceAdmin(admin.ModelAdmin):
    
    list_display = ('role',)
    search_fields = ('role','company')
    
class JobAdmin(admin.ModelAdmin):
    
    list_display = ('title',)
    search_fields = ('title',)
    
class EventsAdmin(admin.ModelAdmin):
    
    list_display = ('title',)
    search_fields = ('title',)
    


    
admin.site.register(LinkedinUser,LinkedinUserAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(ProfessionalExperience,ProfessionalExperienceAdmin)
admin.site.register(Job,JobAdmin)
admin.site.register(Events,EventsAdmin)
    
# Register your models here.

