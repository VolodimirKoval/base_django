from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
    