from django.shortcuts import render
from .models import YearFolder, YearElement
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def archivePage(request):
    year = YearFolder.objects.all()[::-1]
    if not year:
        return render(request, '404.html')
    return render(request, 'archive/index.html', {'years': year})

def archiveElementPage(request, year):
    element = YearElement.objects.filter(anno=year).all()
    if not element:
        return render(request, '404.html')
    return render(request, 'archive/archive.html', {'element': element})