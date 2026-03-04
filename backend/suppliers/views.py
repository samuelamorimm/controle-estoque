from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import SupplierSerializer
from .models import Supplier

#view de fornecedores
class SupplierView(APIView):
    
    #criar um fornecedor
    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Fornecedor cadastrado com sucesso!",
                "supplier": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "message": "Erro ao cadastrar fornecedor, confira as informações e tente novamente!",
        },status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk=None): #pk=None significa que não é obrigatório passar id na requisição
        
        if pk: #se tiver id, valida e retorna o especifíco
            try:
                supplier = Supplier.objects.get(pk=pk)
                serializer = SupplierSerializer(supplier)
                return Response({
                    "supplier": serializer.data
                }, status=status.HTTP_200_OK)
            except Supplier.DoesNotExist:
                return Response({
                    "message": "Fornecedor não encontrado!"
                }, status=status.HTTP_404_NOT_FOUND)
        else: #se não, retorna todos os fornecedores
            suppliers = Supplier.objects.all()
            if suppliers.exists():
                return Response({
                    "suppliers": SupplierSerializer(suppliers, many=True).data
                }, status=status.HTTP_200_OK)
            
            return Response({
                "message": "Você não possui fornecedores cadastrados!"
            }, status=status.HTTP_404_NOT_FOUND)         
    
    #atualizar um fornecedor
    def patch(self, request, pk):
        
        try:
            supplier = Supplier.objects.get(pk=pk) #verifica se existe o fornecedor com o id passado na requisição
        except Supplier.DoesNotExist: # se o mesmo não existir retorna uma resposta
            return Response({
                "message": "Fornecedor não encontrado"
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SupplierSerializer(supplier, data=request.data, partial=True) #existindo converte o mesmo pra json, partial=True -> atualiza só os campos passados
        if serializer.is_valid(): #verifica se o serializer é válido
            serializer.save() #salva o serializer 
            return Response({
                "message": "Fornecedor atualizado com sucesso!",
                "supplier": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({ #caso não entre em nenhuma validação retorna esse erro
            "Não foi possível atualizar o fornecedor. Tente novamente!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    #excluir um fornecedor   
    def delete(self, request, pk):
        
        try:
            supplier = Supplier.objects.get(pk=pk)
            supplier.delete()
            return Response({
                "message": "Fornecedor excluído com sucesso!"
            }, status=status.HTTP_200_OK)
        except Supplier.DoesNotExist:
            return Response({
                "message": "Fornecedor não encontrado!"
            }, status=status.HTTP_404_NOT_FOUND)
                    