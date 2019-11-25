from django.shortcuts import render

# Create your views here.
def index(request):
    """render the home page"""
    return render(request, 'meal_plans/index.html')