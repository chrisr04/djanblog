from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('autores/',autor, name="autores"),
    path('<str:category>/',categoria, name="categoria"),
    path('<str:category>/<slug:slug>/',publicacion, name = 'publicacion'),
]

