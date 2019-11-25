from django.shortcuts import render
from pizzas.models import Pizza, Topping

# Create your views here.
def index(request):
    """render the home page"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """show all pizzas"""
    pizzas = Pizza.objects.all()
    context = {
        'pizzas': pizzas
    }
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """show the detail of pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {
        'pizza': pizza,
        'toppings': toppings,
    }
    return render(request, 'pizzas/pizza.html', context)