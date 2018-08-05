from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from django.contrib.gis.db import models as modelss
# Create your models here.

class Neighbor_hood(models.Model):
	name=models.CharField(max_length=100, null=True, blank=True)
	location=modelss.PointField()
	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']	

	def save_hood(self):
		self.save()	

	@classmethod
	def find_neighbor_hood(cls,hood_id):
		hood=cls.objects.filter(id=hood_id)
		return hood	
