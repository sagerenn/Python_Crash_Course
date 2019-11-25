from django.urls import path, include
from users import views

app_name = 'users'
urlpatterns = [
    # include default auth urls
    path('', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
]
