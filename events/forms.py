from django.forms import ModelForm, DateInput
from events.models import Events

class CreateEventForm(ModelForm):
    class Meta:
        model = Events
        fields = ['title','description','date','photo', 'category']
        widgets = {
            'date': DateInput(attrs={'type':'date'})
        }