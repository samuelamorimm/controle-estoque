from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from accounts.models import CustomUser
from .serializers import UserSerializer

def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("Usuário inativo!")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

#registra um usuário
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                "message":'Usuário registrado com sucesso!',
                "user": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
            
        username = request.data.get('username')
        validated_user = CustomUser.objects.filter(username=username).first()
        if validated_user:
            return Response({
                "message": "Usuário já existe!"
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            "message":"Erro ao cadastrar usuário. Verifique suas informações e tente novamente!"
        }, status=status.HTTP_400_BAD_REQUEST)

#View de autenticação       
class LoginUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        response_erro = Response({
            "message": "Credenciais inválidas. Verifique suas informações e tente novamente!"
        }, status=status.HTTP_400_BAD_REQUEST)
        
        response_not_admin = Response({
            "message": "Você não tem permissão para acessar este recurso. Contate um administrador caso precise de acesso."
        }, status=status.HTTP_400_BAD_REQUEST)
        
        #Verifica se usuário existe
        user = CustomUser.objects.filter(username=username).exists()
        if not user:
            return response_erro
        
        #filtra o usuário caso exista
        user = CustomUser.objects.filter(username=username).first()
        
        #verifica se é adm
        if not user.is_superuser:
            return response_not_admin
        
        #verifica senha
        if not check_password(password, user.password):
            return response_erro
        
        #gera token e efetua login
        token = get_tokens_for_user(user)
        return Response({
            "message": "Usuário autenticado com sucesso!",
            "user": user.username,
            "user_id": user.id,
            "user_token": token['access'] 
        }, status=status.HTTP_200_OK)


