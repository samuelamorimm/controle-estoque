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
            
    #retornar todos os produtos
    def get(self, request):       
        products = Product.objects.all()
        if products:
            return Response({
                "products": products,
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Erro ao buscar todos os produtos. Tente novamente em alguns minutos!"
        }, status=status.HTTP_400_BAD_REQUEST)