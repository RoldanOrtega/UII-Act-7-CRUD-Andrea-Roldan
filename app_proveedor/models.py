from django.db import models

# Create your models here.
class proveedores(models.Model):
    nombre_empresa = models.CharField(max_length=100)
    contacto_nombre = models.CharField(max_length=50)
    contacto_telefono = models.CharField(max_length=15)
    contacto_email = models.EmailField()
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_empresa
