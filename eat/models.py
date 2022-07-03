from django.db import models

# Create your models here.
class Menu(models.Model):
    image = models.ImageField(upload_to='menu', blank=True, null=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    menu = models.ManyToManyField(Menu, related_name='orders')
    date = models.DateTimeField(auto_now_add=True)