from django.db import models

# Create your models here.
class YearFolder(models.Model):
    anno = models.CharField(max_length=90)

    def __str__(self):
        return 'Cartella anno ' + self.anno

class YearElement(models.Model):
    anno = models.CharField(max_length=90)
    data = models.CharField(max_length=90)
    parte = models.IntegerField()
    video = models.URLField()
    convocazione = models.FileField()
    nota = models.TextField(blank=True)

    def __str__(self):
        return 'Elementi anno ' + self.anno