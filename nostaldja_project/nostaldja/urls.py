from django.urls import path
from . import views

urlpatterns = [
    path('', views.decade_list, name='decade_list'),
    path('decades', views.decade_list, name='decade_list'),
    path('decades/new', views.decade_create, name='decade_create'),
    path('decades/<int:pk>', views.decade_detail, name='decade_detail'),
    path('decades/<int:pk>/edit', views.decade_update, name='decade_update'),
    path('decades/<int:pk>/delete', views.decade_delete, name='decade_delete'),

    path('fads', views.fad_list, name='fad_list'),
    path('fads/new', views.fad_create, name='fad_create'),
    path('fads/<int:pk>', views.fad_detail, name='fad_detail'),
    path('fads/<int:pk>/edit', views.fad_update, name='fad_update'),
    path('fads/<int:pk>/delete', views.fad_delete, name='fad_delete'),
]