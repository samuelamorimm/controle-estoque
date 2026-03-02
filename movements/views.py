from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movement
from .serializers import MovementSerializer

# Create your views here.
def update_stock(product, old_quantity, old_type, updated_movement): #função para atualizar o estoque conforme atualizações nas movimentações
                
    if old_type == 'IN': #se valor antigo for entrada
        if updated_movement.type == 'IN': #atualiza a quatidade do estoque se for entrada
            product.quantity = (product.quantity - old_quantity) + updated_movement.quantity
        elif updated_movement.type == 'OUT': #atualiza a quantidade do estoque se for saída
            product.quantity = (product.quantity - old_quantity) - updated_movement.quantity
    elif old_type == 'OUT': #se valor antigo for saída
        if updated_movement.type == 'IN': #atualiza a quatidade do estoque se for entrada
            product.quantity = (product.quantity + old_quantity) + updated_movement.quantity
        elif updated_movement.type == 'OUT': #atualiza a quantidade do estoque se for saída
            product.quantity = (product.quantity + old_quantity) - updated_movement.quantity
    
    product.save() #atualiza estoque do produto

def delete_stock_update(product, type_movement, quantity_movement):
    if type_movement == 'IN':
        product.quantity -= quantity_movement
    elif type_movement == 'OUT':
        product.quantity += quantity_movement
        
    product.save()

class MovementView(APIView):
    
    #cadastrar uma movimentação
    def post(self, request):
        serializer = MovementSerializer(data=request.data)
        
        if serializer.is_valid():
            movement = serializer.save()
            product = movement.product #Pega o produto da movimentação
            
            if movement.type == 'IN': #se for entrada, adiciona no estoque do produto
                product.quantity += movement.quantity
                product.save()
            elif movement.type == 'OUT': #se for saida
                if product.quantity < movement.quantity:#verifica se o produto tem quantidade suficiente para saída
                    return Response({
                        "message": "Estoque insuficiente para saída!"
                    }, status=status.HTTP_400_BAD_REQUEST)
                product.quantity -= movement.quantity
                product.save()
            
            return Response({
                "message": "Movimentação cadastrada com sucesso!",
                "movement": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            "Não foi possível cadastrar a movimentação, verifique as informações e tente novmamente!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    #pegar uma ou todas movimentações    
    def get(self, request, pk=None):
        
        if pk:
            try:
                movement = Movement.objects.get(pk=pk)
                serializer = MovementSerializer(movement)
                return Response({
                    "movement": serializer.data
                })
            except Movement.DoesNotExist:
                return Response({
                    "message": "Movimentação não encontrada!"
                }, status=status.HTTP_404_NOT_FOUND)
        else:
            movements = Movement.objects.all()
            if movements.exists():
                return Response({
                    "movements": MovementSerializer(movements, many=True).data
                }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Você não possui nenhuma movimentação cadastrada!"
        }, status=status.HTTP_404_NOT_FOUND)
    
    #atualizar uma movimentação
    def patch(self, request, pk):
        
        try:
            movement = Movement.objects.get(pk=pk) #busca movimentação
        except Movement.DoesNotExist: #caso ela não exista, retorna erro
            return Response({
                "message": "Movimentação não encontrada!"
            }, status=status.HTTP_404_NOT_FOUND)
        
        old_quantity = movement.quantity #quantidade antinga do movimento
        old_type = movement.type #Tipo antigo
        serializer = MovementSerializer(movement, data=request.data, partial=True)
        
        if serializer.is_valid():
            updated_movement = serializer.save() #movimentação atualizada
            product = updated_movement.product #produto

            update_stock(product, old_quantity, old_type, updated_movement) #chama função para atualizar estoque
            
            return Response({
                "message": "Movimentação atualizada com sucesso!",
                "movement": MovementSerializer(updated_movement).data,
                "product_stock": product.quantity
            }, status=status.HTTP_200_OK)
        
        return Response({
            "message": "Erro ao atualizar movimentação. Tente novamente!"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            movement = Movement.objects.get(pk=pk)
            type_movement = movement.type
            quantity_movement = movement.quantity
            product = movement.product
            
            delete_stock_update(product, type_movement, quantity_movement) #atualiza estoque ao deletar movimentação
            
            movement.delete()
            return Response({
                "message": "Movimentação excluída com sucesso!"
            }, status=status.HTTP_200_OK)
        except Movement.DoesNotExist:
            return Response({
                "message": "Movimentação não encontrada!"
            }, status=status.HTTP_400_BAD_REQUEST)