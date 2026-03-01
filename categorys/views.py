from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer
from .models import Category

#View de categorias
class CategoryView(APIView):
    
    #criar uma categoria
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            category = serializer.save()
            return Response({
                "message": "Categoria criada com sucesso!",
                "category": CategorySerializer(category).data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Erro ao criar categoria, preencha todos os campos corretamente!",
        }, status=status.HTTP_400_BAD_REQUEST)
        
    #pegar todas as categorias ou uma específica
    def get(self, request, pk=None):
        
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response({
                    "category": serializer.data
                }, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({
                    "message": "Categoria não encontrada!",
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            categorys = Category.objects.all()
            if categorys.exists():
                serializer = CategorySerializer(categorys, many=True)
                return Response({"categorys": serializer.data}, status=status.HTTP_200_OK)
            
            return Response({
                    "message": "Você não possui categorias cadastradas!",
                }, status=status.HTTP_400_BAD_REQUEST)
    
    #atualizar uma categoria
    def patch(self, request, pk):
        
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({
                "message":"Categoria não encontrada!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Categoria atualizada com sucesso!",
                "category": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Erro ao atualizar categoria!",
        }, status=status.HTTP_400_BAD_REQUEST)
    
    #excluir uma categoria
    def delete(self, request, pk):
        
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({
                "message": "Categoria excluída com sucesso!"
            }, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({
                "message": "Categoria não encontrada!"
            }, status=status.HTTP_404_NOT_FOUND)