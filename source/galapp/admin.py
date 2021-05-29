from django.contrib import admin

from galapp.models import Albom, Photos, Chosen


class PhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'foto', 'text', 'created_at', 'user']
    list_filter = ['text']
    search_fields = ['text']
    fields = ['id', 'text', 'foto', 'user', 'is_private', 'album', 'created_at' ]
    readonly_fields = ['id', 'created_at']

admin.site.register(Photos, PhotosAdmin)
admin.site.register(Albom)
admin.site.register(Chosen)