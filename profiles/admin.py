
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import UserProfile, Item

class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = UserProfile

admin.site.register(UserProfile, profileAdmin)
admin.site.register(Item)