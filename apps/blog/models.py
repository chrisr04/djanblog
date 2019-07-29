from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, null = False,blank = False)
    imagen = models.URLField(max_length = 255, blank = False, null= False, default="https://www.info-computer.com/blog/wp-content/uploads/2018/04/fotoinicio.jpg")
    activo = models.BooleanField( default = True)
    creado = models.DateField(auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 255, null = False, blank = False)
    apellido = models.CharField(max_length = 255, null = False, blank = False)
    correo = models.EmailField(blank = False, null = False)
    foto = models.URLField(max_length = 355, blank = True, null= True, default="https://www.uic.mx/posgrados/files/2018/05/default-user.png")
    fondo = models.URLField(max_length = 355, blank = True, null= True, default="https://sc2.elpais.com.uy/files/article_default_content/uploads/2017/11/27/5a1c86989e3eb.jpeg")
    facebook = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    instagram = models.URLField(null = True, blank = True)
    activo = models.BooleanField(default = True)
    creado = models.DateField(auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Publicacion(models.Model):
    id = models.AutoField(primary_key = True)
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    titulo = models.CharField('Título', max_length = 100, blank = False, null = False)
    slug = models.CharField('Slug', max_length = 100, blank = False, null = False)
    descripcion = models.CharField('Descripción', max_length = 110, blank = False, null = False)
    contenido = RichTextField()
    imagen = models.URLField(max_length = 255, blank = False, null= False)
    activo = models.BooleanField(default = True)
    creado = models.DateField(auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo