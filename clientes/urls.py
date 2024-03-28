# clientes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
    path('<int:cliente_id>/eliminar/', views.eliminar_cliente, name='eliminar_cliente'),
    path('about_us/', views.about_us, name='about_us'),  # Nueva ruta para "About Us"
]
