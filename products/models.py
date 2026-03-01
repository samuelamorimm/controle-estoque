from django.db import models

class Provider(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    
    class Meta:
        db_table = 'provider'
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    
    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='providers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorys')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'products'
    
    def __str__(self):
        return self.name