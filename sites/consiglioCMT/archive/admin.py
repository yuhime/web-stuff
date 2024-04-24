from django.contrib import admin
from .models import YearElement, YearFolder

# Register your models here.
admin.site.register(YearFolder)
admin.site.register(YearElement)