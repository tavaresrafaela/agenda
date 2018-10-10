from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('cad/list', views.cad_list, name='cad-list'),
    path('cad/<int:pk>/', views.cad_detail, name='cad-detail'),
    path('cad/new', views.cad_new, name='cad-new'),
    path('cad/<int:pk>/edit/', views.cad_edit, name='cad-edit'),


]
