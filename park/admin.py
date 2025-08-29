from django.contrib import admin
from .models import Park, Entertainment, EntertainmentPhoto

class EntertainmentPhotoInline(admin.StackedInline):
    model = EntertainmentPhoto
    fields = ('photo',)
    extra = 1

class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'park', 'price')
    inlines = [EntertainmentPhotoInline]

admin.site.register(Park)
admin.site.register(Entertainment, EntertainmentAdmin)
