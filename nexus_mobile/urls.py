from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required as auth
from tastypie.api import Api
from api import CurrentReadingResources
from api import HourlyReadingResources
from api import DailyReadingResources
from api import MonthlyReadingResources
from api import DeviceResources
from api import UserResource
#from api import UserProfileResources
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CurrentReadingResources())
v1_api.register(HourlyReadingResources())
v1_api.register(DailyReadingResources())
v1_api.register(MonthlyReadingResources())
v1_api.register(DeviceResources())
#v1_api.register(UserProfileResources())
v1_api.register(UserResource())



urlpatterns = patterns('',	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api/', include(v1_api.urls)),
)
