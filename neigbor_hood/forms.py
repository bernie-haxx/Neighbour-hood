from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from floppyforms.gis import PointWidget, BaseGMapWidget
from .models import UserProfile,Neighbor_hood,Business


class NewProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user'] 
