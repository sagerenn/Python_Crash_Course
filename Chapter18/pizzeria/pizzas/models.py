from django.db import models

# Create your models here.
class Pizza(models.Model):
    """a specific pizza"""
    name = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """representation of pizza"""
        return self.name

class Topping(models.Model):
    """specific toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """representation of pizza"""
        return self.name