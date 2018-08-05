from django.contrib import admin

from .models import UserProfile,Neighbor_hood,Business
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Neighbor_hood)
admin.site.register(Business)
