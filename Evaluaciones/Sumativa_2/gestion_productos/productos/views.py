# productos/views.py
from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
 
# Vista para listar productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})
 
# Vista para registrar un producto (solo accesible para usuarios autenticados)
@login_required
def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultado_producto')
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})
 
# Vista para mostrar el resultado de la creación
def resultado_producto(request):
    return render(request, 'productos/resultado.html')
 
# Vista para mostrar la consulta de productos
def consulta(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})
