from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('posts/<int:number_post>/', views.posts_by_number),
    path('posts/<str:name_post>/', views.posts),
    path('posts', views.show_all_posts),
]
