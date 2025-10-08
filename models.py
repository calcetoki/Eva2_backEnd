from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField()
    prioridad = models.IntegerField(default=3)
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_limite = models.DateField(null=True, blank=True)
 
    class Meta:
        ordering = ['-fecha_creacion']
 
    def __str__(self):
        return self.titulo
    
