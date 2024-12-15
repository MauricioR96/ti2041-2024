# productos/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from datetime import datetime
from django.http import HttpResponse
 
# Vista para listar productos (solo accesible para usuarios autenticados)
@login_required
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos, 'user': request.user})
 
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
 
# Vista para actualizar un producto (solo accesible para usuarios autenticados)
@login_required
def actualizar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/actualizar.html', {'form': form, 'producto': producto})
 
# Vista para eliminar un producto (solo accesible para usuarios autenticados)
@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'productos/eliminar_confirmacion.html', {'producto': producto})
 
# Vista para mostrar el resultado de la creación
def resultado_producto(request):
    return render(request, 'productos/resultado.html')
 
# Vista para mostrar la consulta de productos
@login_required
def consulta(request):
    productos = Producto.objects.all()
    return render(request, 'productos/consulta.html', {'productos': productos})
 
# Vista de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Guardar variables en la sesión
            request.session['username'] = username
            request.session['login_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request.session['is_admin'] = user.groups.filter(name='ADMIN_PRODUCTS').exists()
            return redirect('lista_productos')
        else:
            return render(request, 'productos/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'productos/login.html')
 
# Vista de logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
 
# Vista protegida para productos
@login_required
def productos_view(request):
    if not request.session.get('is_admin', False):
        return HttpResponse("No tienes permisos para acceder a esta página.", status=403)
    return render(request, 'productos/index.html')