from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class UserProfile(models.Model):
	name = models.CharField(max_length = 120)
	description = models.TextField(default='description default text')

	def __unicode__(self):
		return self.name

class Item(models.Model):
	owner = models.ForeignKey(User, related_name= 'items')
	item_name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	price = models.IntegerField(default = 0);
	picture = models.FileField()
	when_created = models.DateTimeField(auto_now_add = True)

	
	def __str__(self):
		return '{} owned by: {}'.format(self.item_name, self.owner.username)
