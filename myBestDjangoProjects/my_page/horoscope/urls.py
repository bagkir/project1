from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # path('guinness/', views.get_guinness_world_records),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<int:month>/<int:day>/', views.sign_zodiac),
    path('type/', views.get_info_about_types),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('type/<str:element>/', views.get_info_about_sign_zodiac_from_types, name='horoscope-typezodiacs'),
    # path('show_data_actors/<int:year_born>/<str:city_born>/<str:movie_name>/', views.info_about_actors),
]
