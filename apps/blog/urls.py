from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'home'),
    path('<str:category>/',categoria, name="categoria"),
    path('<str:category>/<slug:slug>/',detallePost, name = 'detalle_post'),
]

