from django.contrib import admin
from .models import UserProfile,Neighbor_hood,Business
from leaflet.admin import LeafletGeoAdmin
from leaflet.admin import LeafletGeoAdminMixin
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Neighbor_hood, LeafletGeoAdmin)
admin.site.register(Business)
