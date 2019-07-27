from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','imagen','activo','creado',)
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre','apellido','correo']
    list_display = ('nombre','apellido','correo','activo','creado',)
    resource_class = AutorResource

class PublicacionResource(resources.ModelResource):
    class Meta:
        model = Publicacion

class PublicacionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo','descripcion']
    list_display = ('titulo','slug','descripcion','activo','creado',)
    resource_class = PublicacionResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Publicacion,PublicacionAdmin)