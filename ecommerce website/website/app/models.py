from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=45)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='shops')
    rating = models.TextField(max_length=10,default="⭐⭐⭐")
    def __str__(self):
        return self.name

