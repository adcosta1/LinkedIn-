from django.forms import ModelForm,DateInput
from jobs.models import Job
class PublishJobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'deadline_date', 'category', 'link','photo','state']
        widgets = {
            'deadline_date': DateInput(attrs={'type':'date'})
        }