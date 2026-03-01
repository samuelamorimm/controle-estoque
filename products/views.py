from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

#view de produtos
class ProductView(APIView):
    
    #cadastrar produto
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            product = serializer.save()
            
            return Response({
                "message": "Produto cadastrado com sucesso!",
                "product": ProductSerializer(product).data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
                "message": "Erro ao cadastrar produto, verifique as informações e tente novamente!",
            }, status=status.HTTP_400_BAD_REQUEST)
            
    #retornar todos os produtos ou um específico
    def get(self, request, pk=None):
        
        if pk:
            try:
                product = Product.objects.get(pk=pk)
                serializer = ProductSerializer(product)
                return Response({
                    "product": serializer.data
                }, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({
                    "message": "Produto não encontrado!"
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            if products.exists():
                serializer = ProductSerializer(products, many=True)
                return Response({
                    "products": serializer.data,
                }, status=status.HTTP_200_OK)
            
            return Response({
                "message": "Erro ao buscar todos os produtos. Tente novamente em alguns minutos!"
            }, status=status.HTTP_400_BAD_REQUEST)
        
    #atualizar um produto
    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({
                "message": "Produto não encontrado!"
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Produto atualizado com sucesso!",
                "product": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Erro ao atualizar produto",
        }, status=status.HTTP_400_BAD_REQUEST)
    
    #deletar um produto
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response({
                "message": "Produto excluído com sucesso!"
            }, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({
                "message": "Produto não encontrado!"
            }, status=status.HTTP_404_NOT_FOUND)