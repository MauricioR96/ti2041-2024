# productos/views.py
from django.shortcuts import render
 
# Almacena los productos en memoria
productos = []
 
def index(request):
    return render(request, 'productos/index.html')
 
def registro(request):
    if request.method == 'POST':
        # Obtén los datos del formulario y agrégalos a la lista de productos
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        marca = request.POST['marca']
        fecha_vencimiento = request.POST['fecha_vencimiento']
        producto = {'codigo': codigo, 'nombre': nombre, 'marca': marca, 'fecha_vencimiento': fecha_vencimiento}
        productos.append(producto)
        return render(request, 'productos/resultado.html', {'producto': producto})
    return render(request, 'productos/registro.html')
 
def resultado(request):
    return render(request, 'productos/resultado.html')
 
def consulta(request):
    return render(request, 'productos/consulta.html', {'productos': productos})