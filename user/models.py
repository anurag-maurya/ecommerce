from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quentity = models.PositiveIntegerField()
    
    class Meta:
        unique_together = ["user", "product"]
    
    def __str__(self):
        return f"{self.user.username} - Cart"