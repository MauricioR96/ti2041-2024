from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from .models import Producto
from .serializers import ProductoSerializer
 
class ProductoViewSet(viewsets.ModelViewSet):
    """
    API para gestionar productos:
    - GET: Listar todos los productos
    - POST: Crear un producto
    - PUT: Actualizar un producto
    - DELETE: Eliminar un producto
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
 
class TokenView(APIView):
    """
    Servicio para obtener un token JWT.
    Parámetros:
    - username
    - password
    """
    permission_classes = []
 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
 
class ProductoListView(APIView):
    """
    Listar productos o crear uno nuevo.
    """
    permission_classes = [IsAuthenticated]
 
    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
 
class ProductoDetailView(APIView):
    """
    Obtener, actualizar o eliminar un producto.
    """
    permission_classes = [IsAuthenticated]
 
    def get(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
 
    def put(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
    def delete(self, request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)