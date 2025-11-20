from django.db import models

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('alimentos', 'Alimentos'),
        ('hogar', 'Hogar'),
        ('deportes', 'Deportes'),
        ('otros', 'Otros'),
    ]
    
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, default='otros', verbose_name="Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-fecha_creacion']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
