from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from djgeojson.fields import PointField
from jsonfield import JSONField
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

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
	ID=models.CharField(max_length=100, null=True, blank=True)
	profilepicture = models.ImageField(upload_to='images/', blank=True,default="/black.png")
	neighbor_hood=models.ForeignKey(Neighbor_hood, on_delete=models.CASCADE,related_name="hood",null=True,blank=True)
	secondary_email = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.user
	class Meta:
		ordering = ['user']
	def save_user(self):
		self.save()
	def delete_user(self):
		self.delete()		

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
				UserProfile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

class Business(models.Model):
	name=models.CharField(max_length=100, null=True, blank=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="business",null=True,blank=True)
	neighbor_hood=models.ForeignKey(Neighbor_hood, on_delete=models.CASCADE,related_name="hoodbus",null=True,blank=True)
	email = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ['name']	

	def save_business(self):
		self.save()	
	def delete_business(self):
		self.delete()		

	@classmethod
	def find_business(cls,business_id):
		business=cls.objects.filter(id=business_id)
		return business			

	@classmethod
	def search_by_title(cls,search_term):
		business = cls.objects.filter(title__icontains=search_term)
		return business		