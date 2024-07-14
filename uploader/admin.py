from django.contrib import admin

from .models import MediaUser

@admin.register(MediaUser)
class MediaUserAdmin(admin.ModelAdmin):
	list_display = ('id', 'file')
	search_fields = ('file',)
	ordering = ('id',)
	list_per_page = 20
	