from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'), # O la vista que corresponda
    path('<int:id>/', views.ver_proveedores, name='ver_proveedor'),
    path('agregar/', views.agregar_proveedores, name='agregar_proveedor'),
    path('editar/<int:id>/', views.editar_proveedor, name='editar_proveedor'),
    path('borrar/<int:id>/', views.borrar_proveedores, name='borrar_proveedor'),
]