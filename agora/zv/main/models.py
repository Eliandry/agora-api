from django.db import models
class Product(models.Model):
    product_id = models.CharField(max_length=60)
    name = models.CharField(max_length=1000)
    reference_id = models.CharField(max_length=100)
    def __str__(self):
        return self.product_id

