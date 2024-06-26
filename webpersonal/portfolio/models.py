from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to="projects")
    link = models.URLField(verbose_name='Dirección web', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación') #auto_add_now Se actualiza solo al crearlo#
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización') #auto_now se actualiza siempre que haya un cambio#
    

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"] #Con esto ordenamos. Al ponerle el - ordena de más nuevo a más viejo#

    def __str__(self):
        return self.title
    