from django.urls import path
from . import views
urlpatterns = [
    path('<int:day>/', views.the_chousen_day_by_number),
    path('people_detail', views.get_info_about_people, name='week-name'),
    # path('people', views.get_info_about_people, name='week-name'),
    path('<str:day>/', views.the_chousen_day, name='week-name'),
    # path('views/', views.tuesday),
]
