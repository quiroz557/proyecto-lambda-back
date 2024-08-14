from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import render
from django.http import HttpResponse

@api_view(['POST'])
def registro(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    cedula = request.data.get('cedula')
    telefono = request.data.get('telefono')

    user = User.objects.create(username=username, password=password, email=email)

    return Response({"message": "Usuario creado exitosamente."}, status=status.HTTP_201_CREATED)

    # Verifica si falta algún dato requerido
    if not all([username, password, email, cedula, telefono]):
        return Response({"error": "Faltan datos obligatorios."}, status=status.HTTP_400_BAD_REQUEST)

    # Verifica si el usuario ya existe
    if User.objects.filter(username=username).exists():
        return Response({"error": "El usuario ya existe."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Crea el usuario en el modelo User
        

        # Crea el perfil de usuario en UserProfile
        user_profile = UserProfile.objects.create_user(user=user, nombre=username, correo=email, cedula=cedula, telefono=telefono)

        
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def login(request):
    users = UserProfile.objects.all()  # Obtén todos los usuarios de UserProfile
    serializer = UserProfileSerializer(users, many=True)  # Serializa los datos
    return Response(serializer.data)  # Devuelve los datos en la respuesta

@api_view(['POST'])
def logout(request):
    # Implementar la lógica de cierre de sesión.
    pass

def login(request):
    return HttpResponse("Página de inicio de sesión")

def logout(request):
    return HttpResponse("Página de cierre de sesión")

def home(request):
    return HttpResponse("Página de inicio")