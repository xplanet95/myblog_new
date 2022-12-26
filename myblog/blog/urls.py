from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('category/<str:slug>/', views.get_category, name='get_category'),
    path('post/<str:slug>/', views.get_post, name='post'),
]
