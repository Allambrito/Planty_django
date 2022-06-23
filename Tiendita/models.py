
from django.db import models
from django.forms import ImageField

# Create your models here.

class Producto(models.Model):
    Nombre_producto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    Precio_producto = models.CharField(max_length=10, verbose_name='Precio del producto')
    Foto_producto = models.ImageField(null=True, blank=True, upload_to="")
    Descripcion_producto = models.TextField(max_length=50, verbose_name='Descripcion del producto')
    
    def __str__(self):
        return self.Nombre_producto




class Usuario(models.Model):
    Nombre_usuario = models.CharField(max_length=15, verbose_name='Nombre de usuario')
    Password_usuario = models.CharField(max_length=10, verbose_name='Password del usuario')



