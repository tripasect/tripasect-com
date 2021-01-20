from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.university, name='main-university'),
    path('linear-algebra/', views.linear_algebra, name='university-linear-algebra'),
    path('advanced-programming/', views.advanced_programming, name='university-linear-algebra'),
    path('advanced-programming/vocabulary', include('vocabulary.urls')),
    path('basic-programming/', views.basic_programming, name='university-basic-programming'),
]
