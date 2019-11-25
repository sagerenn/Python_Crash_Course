from django.urls import path
from blogs import views

app_name = 'blogs'
urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_post/', views.add_post, name='add_post'),
]
