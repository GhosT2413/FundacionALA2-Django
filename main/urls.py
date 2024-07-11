from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('chifu/', views.chifu, name='chifu'),
    path('contact/', views.contact, name='contact'),
    path('donar/', views.donar, name='donar'),
    path('login/', views.login, name='login'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('perfil/', views.perfil, name='perfil'),
    path('rayo/', views.rayo, name='rayo'),
    path('signup/', views.signup, name='signup'),
    path('winnie/', views.winnie, name='winnie'),
    path('woody/', views.woody, name='woody'),
]