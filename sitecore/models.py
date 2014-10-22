from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from django.core.urlresolvers import reverse


class Device(models.Model):
	user = models.ForeignKey(User, related_name = "devices")
	device_identifier = models.CharField(max_length= 16)

	def __unicode__(self):
		return self.device_identifier


class CurrentReading(models.Model):
	device_id = models.ForeignKey(Device, related_name="current_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField('time period')

	def __unicode__(self):
		return self.created_at.strftime('%Y-%m-%d %I:%M%p')


class HourlyReading(models.Model):
	device_id = models.ForeignKey(Device, related_name="hourly_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField('time period')

	def __unicode__(self):
		return self.created_at.strftime('%Y-%m-%d %I:%M%p')


class DailyReading(models.Model):
	device_id = models.ForeignKey(Device, related_name="daily_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.created_at.strftime('%Y-%m-%d')


class MonthlyReading(models.Model):
	device_id = models.ForeignKey(Device, related_name="monthly_readings")
	kWh = models.DecimalField(max_digits=6, decimal_places=4)
	cost  = models.DecimalField(max_digits=6, decimal_places=4)
	created_at= models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField()

	def __unicode__(self):
		return self.created_at.strftime('%Y-%m-%d')