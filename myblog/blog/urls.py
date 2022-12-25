from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:slug>/', views.get_category, name='get_category'),
]
