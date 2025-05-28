from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import StudentUser, Classroom
from .models import Profile

class StudentRegistrationForm(UserCreationForm):
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all(), required=True)
    class Meta:
        model = StudentUser
        fields = ['first_name', 'last_name', 'username', 'email', 'classroom', 'password1', 'password2']


# Profile Picture
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']