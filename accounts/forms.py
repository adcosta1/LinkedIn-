from django.forms import DateInput
from accounts.models import LinkedinUser
from django.contrib.auth.forms import UserCreationForm

class CreateuserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = LinkedinUser
        fields = ['first_name', 'last_name', 'username', 'gender', 'DOB', 'Bio', 'Race', 'email', 'state','category','photo']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})
        }