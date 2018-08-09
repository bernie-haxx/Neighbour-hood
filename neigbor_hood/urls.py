from django.conf.urls import url
from .  import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
url(r'^$',views.home,name='home'),
url(r'^new_profile/$',views.new_profile,name='new_profile'),
url(r'^new_neigbor_hood/$',views.new_neigbor_hood,name='new_hood'),
url(r'^new_business/$',views.new_business,name='new_business'),
url(r'^new_post/$',views.new_post,name='new_post'),
url(r'^hood_business/$',views.hood_business,name='hood_business'),
url(r'^search/',views.search_results,name='search'),
url(r'^join_hood/(?P<hood_id>\d+)',views.follow_hood,name='join_hood'),
url(r'^hood/(?P<hooder_id>\d+)',views.hoods,name='hoods'),
url(r'^hood_home/',views.neigbor_hood,name='neigbor_hood'),
url(r'^hooder/(?P<post_id>\d+)?$',views.hooder,name='hood')
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
