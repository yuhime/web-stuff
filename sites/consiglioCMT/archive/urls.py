from django.urls import path, re_path
from . import views

urlpatterns = [
    path('archive/', views.archivePage),
    re_path(r'^archive/(?P<year>.+)', views.archiveElementPage),
]
