from django.contrib import admin
from.models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
	list_display = ['name','surname','pay']
	list_display_links = ['name']