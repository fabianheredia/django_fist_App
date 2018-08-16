from django.db import models
from datetime import date
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

ITEM_CATEGORIA = (
            ('C','Conferencia'),
            ('S','Seminario'),
            ('Co','Congreso'),
            ('Cu','Curso'),
            )

ITEM_TIPO=(('V','Virtual'),('P','Presencial'))
class Evento(models.Model):
    e_nombre = models.CharField(max_length=200)
    e_categoria=models.CharField(choices=ITEM_CATEGORIA,max_length=1)
    e_lugar= models.CharField(max_length=200)
    e_direccion=models.CharField(max_length=200)
    e_fechaIni =models.DateField(default=date.today)
    e_fechaFin=models.DateTimeField(auto_now=False)
    e_tipo=models.CharField(choices=ITEM_TIPO,max_length=1)
    def __str__(self):
        return self.e_nombre

