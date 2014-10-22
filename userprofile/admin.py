from django.contrib import admin
from .models import UserProfile
from sitecore.models import Device, CurrentReading, HourlyReading, DailyReading, MonthlyReading
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False


class DeviceAdmin(admin.ModelAdmin):
	pass
admin.site.register(Device, DeviceAdmin)


class CurrentReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(CurrentReading, CurrentReadingAdmin)


class HourlyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(HourlyReading, HourlyReadingAdmin)


class DailyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(DailyReading, DailyReadingAdmin)


class MonthlyReadingAdmin(admin.ModelAdmin):
	pass
admin.site.register(MonthlyReading, MonthlyReadingAdmin)


class UserProfileAdmin(UserAdmin):
	inlines = (UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)