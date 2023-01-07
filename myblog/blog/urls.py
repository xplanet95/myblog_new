from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(), name='get_category'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', views.GetPost.as_view(), name='post'),
    path('search/', views.Search.as_view(), name='search'),
]
