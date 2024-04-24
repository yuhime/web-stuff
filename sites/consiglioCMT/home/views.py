from django.shortcuts import render
from .models import HomeSettings

# Create your views here.
def home(request):
    object = HomeSettings.objects.first()
    return render(request, 'home/index.html', {'obj': object})