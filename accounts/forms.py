from django.forms import DateInput
from accounts.models import LinkedinUser,Education,ProfessionalExperience
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm


class CreateuserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = LinkedinUser
        fields = ['first_name', 'last_name', 'username', 'gender', 'DOB', 'Bio', 'Race', 'email', 'state','category','photo']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})
        }
        
class UpdateForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = LinkedinUser
        fields = ['first_name', 'last_name', 'username', 'gender', 'DOB', 'Bio', 'Race', 'email', 'state','category','photo']
        widgets = {
            'DOB': DateInput(attrs={'type': 'date'})
        }
        
class CreateEducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['id', 'graduationyear', 'degreename', 'institutionname']

class CreateProfessionalExperienceForm(ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = ['date_init','date_end', 'role', 'company_name', 'description']
        widgets = {
            'date_init':DateInput(attrs={'type':'date'}),
            'date_end':DateInput(attrs={'type':'date'}),
            }
        