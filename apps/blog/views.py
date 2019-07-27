from django.shortcuts import render
from .models import Publicacion,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    queryset = request.GET.get("buscar")
    categorias = Categoria.objects.filter(activo = True)
    posts = Publicacion.objects.filter(activo = True)
    if queryset:
        posts = Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'posts':posts,'categorias':categorias,'pages':paginator.page_range,'currentPage':posts.number})

def categoria(request,category):
    queryset = request.GET.get("buscar")
    categorias = Categoria.objects.filter(activo = True)
    posts = Publicacion.objects.filter(
        activo = True,
        categoria = Categoria.objects.get(nombre__iexact = category)
    )
    if queryset:
        posts = Publicacion.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            activo = True,
            categoria = Categoria.objects.get(nombre__iexact = category),
        ).distinct()

    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'categorias/category.html',{'posts':posts,'categorias':categorias,'nombre_categoria':category,'pages':paginator.page_range,'currentPage':posts.number})

def detallePost(request,category,slug):
    categorias = Categoria.objects.filter(activo = True)
    post = get_object_or_404(Publicacion,slug = slug)
    return render(request,'publicacion.html',{'detalle_post':post,'categorias':categorias,'nombre_categoria':category})