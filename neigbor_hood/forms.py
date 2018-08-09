from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from floppyforms.gis import PointWidget, BaseGMapWidget
from .models import UserProfile,Neighbor_hood,Business,Post,Comments
from django.contrib import admin
from leaflet.admin import LeafletGeoAdminMixin
from leaflet.forms.widgets import LeafletWidget
class NewProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user'] 
class NewNeigbor_hood_Form(forms.ModelForm):
	class Meta:
		model = Neighbor_hood
		fields = ['name','location']

class New_Business_Form(forms.ModelForm):
	class Meta:
		model = Business
		exclude = ['user'] 		
class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['user']


class NewCommentForm(forms.ModelForm):	
	class Meta:
		model = Comments
		exclude = ['user','date_posted','post']