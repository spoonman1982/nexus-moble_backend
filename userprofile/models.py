from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	COMPARISON_TYPES = (
		('day', 'Daily'),
		('week', 'Weekly'),
		('month', 'Monthly'),
		('year', 'Yearly'),
		)

	daily_target = models.DecimalField(max_digits=8, decimal_places=3, default=0)

	hourly_avg_kwh = models.DecimalField(max_digits=8, decimal_places=3, default=0)
	daily_avg_kwh = models.DecimalField(max_digits=8, decimal_places=3, default=0)
	weekly_avg_kwh = models.DecimalField(max_digits=8, decimal_places=3, default=0)

	daily_cost_target = models.DecimalField(max_digits=7, decimal_places=2, default=0)

	hourly_avg_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	daily_avg_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	monthly_avg_cost = models.DecimalField(max_digits=7, decimal_places=2, default=0)

	last_reading = models.DateTimeField(null=True)
	user_type = models.CharField(max_length=250, null=True)
	device_identifier = models.CharField(max_length=12, null=True)


	@property
	def Targets(self):
		targets = {
		'kwh_daily': self.daily_target,
		'kwh_weekly': self.daily_target * 7,
		'kwh_monthly': self.daily_target * 31,
		'cost_daily': self.daily_cost_target,
		'cost_weekly': self.daily_cost_target * 7,
		'cost_monthly': self.daily_cost_target * 31}
		print targets
		return targets

	def __unicode__(self):
		return "%s's profile" % self.user

def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, created = UserProfile.objects.get_or_create(user=instance)
