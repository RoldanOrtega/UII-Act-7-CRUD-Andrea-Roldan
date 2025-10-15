from django.shortcuts import render, redirect, get_object_or_404
from .models import proveedores as Modeloproveedores

# Listar estudiantes
def index(request):
    proveedores = Modeloproveedores.objects.all() # Usa el nombre renombrado
    return render(request, 'listar_proveedores.html', {'proveedores':proveedores})

# Ver estudiante (opcional, puedes usarlo si quieres detalle)
def ver_proveedores(request, id):
    proveedores = get_object_or_404(proveedores, id=id)
    return render(request, 'ver_proveedores.html', {'proveedores': proveedores})

# Agregar estudiante
def agregar_proveedores(request):
    if request.method == 'POST':
        nombre_empresa = request.POST['nombre_empresa']
        contacto_nombre = request.POST['contacto_nombre']
        contacto_telefono = request.POST['contacto_telefono']
        contacto_email = request.POST['contacto_email']
        direccion = request.POST['direccion']
        Modeloproveedores.objects.create(
            nombre_empresa=nombre_empresa,
            contacto_nombre=contacto_nombre,
            contacto_telefono=contacto_telefono,
            contacto_email=contacto_email,
            direccion=direccion
        )
        return redirect('inicio')
    return render(request, 'agregar_proveedores.html')

# Editar estudiante
def editar_proveedor(request, id):
    proveedores = get_object_or_404(Modeloproveedores, id=id)
    if request.method == 'POST':
        proveedores.nombre_empresa = request.POST['nombre_empresa']
        proveedores.contacto_nombre = request.POST['contacto_nombre']
        proveedores.contacto_telefono = request.POST['contacto_telefono']
        proveedores.contacto_email = request.POST['contacto_email']
        proveedores.direccion = request.POST['direccion']
        proveedores.save()
        return redirect('inicio')
    return render(request, 'editar_proveedores.html', {'proveedores': proveedores})

# Borrar estudiante
def borrar_proveedores(request, id):
    proveedores = get_object_or_404(Modeloproveedores, id=id)
    if request.method == 'POST':
        proveedores.delete()
        return redirect('inicio')
    return render(request, 'borrar_proveedores.html', {'proveedores': proveedores})