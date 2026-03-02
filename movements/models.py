from django.db import models
from products.models import Product

# Models de movimentações
class Movement(models.Model):
    TYPE_CHOICES = [
        ("IN", "In"), #entrada
        ("OUT", "Out"), #saída
    ]
    
    client_name = models.CharField(max_length=200, blank=False, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product')
    type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    amount = models.IntegerField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'movements'
    
    def __str__(self):
        return self.client_name