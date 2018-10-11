from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('cad/list', views.cad_list, name='cad_list'),
    path('cad/<int:pk>/', views.cad_detail, name='cad_detail'),
    path('cad/new', views.cad_new, name='cad_new'),
    path('cad/<int:pk>/edit/', views.cad_edit, name='cad_edit'),


]
