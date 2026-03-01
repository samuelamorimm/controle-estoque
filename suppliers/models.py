from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    
    class Meta:
        db_table = 'provider'
    
    def __str__(self):
        return self.name
