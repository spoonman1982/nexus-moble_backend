from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization
from tastypie.http import HttpUnauthorized, HttpForbidden
from django.conf.urls import url
from tastypie.utils import trailing_slash
from sitecore.models import CurrentReading, HourlyReading, DailyReading, MonthlyReading, Device
#from userprofile.models import UserProfile

class CurrentReadingResources(ModelResource):
	class Meta:
		allowed_methods = ['post', 'get']
		queryset = CurrentReading.objects.all()
		resource_name = 'currentreading'
		authorization = Authorization()

class HourlyReadingResources(ModelResource):
	class Meta:
		allowed_methods = ['post', 'get']
		queryset = HourlyReading.objects.all()
		resource_name = 'hourlyreading'
		authorization = Authorization()

class DailyReadingResources(ModelResource):
	class Meta:
		allowed_methods = ['post', 'get']
		queryset = DailyReading.objects.all()
		resource_name = 'dailyreading'
		authorization = Authorization()

class MonthlyReadingResources(ModelResource):
	class Meta:
		allowed_methods = ['post', 'get']
		queryset = MonthlyReading.objects.all()
		resource_name = 'monthlyreading'
		authorization = Authorization()

class DeviceResources(ModelResource):
	class Meta:
		allowed_methods = ['post', 'get']
		queryset = Device.objects.all()
		resource_name = 'device_resource'
		authorization = Authorization()

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name', 'email',]
        allowed_methods = ['get', 'post']
        resource_name = 'user'
        authentication = 'BasicAuthentication'

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %(self._meta.resource_name, 
                trailing_slash()), self.wrap_view('login'), name="api_login"),
            url(r"^(?P<resource_name>%s)/logout%s$" %(self._meta.resource_name, 
                trailing_slash()), self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.raw_post_data, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                return self.create_response(request, {
                    'username' : user.username,
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)