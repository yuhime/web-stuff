from django.contrib import admin
from .models import HomeSettings

class HomeSettingsAdmin(admin.ModelAdmin):
    actions = ('move')
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super(HomeSettingsAdmin, self).has_add_permission(request)

admin.site.register(HomeSettings, HomeSettingsAdmin)