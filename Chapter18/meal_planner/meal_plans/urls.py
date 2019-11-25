# define the url patterns

from django.urls import path

from meal_plans import views

app_name = 'meal_plans'
urlpatterns = [
    path('', views.index, name='index')
]