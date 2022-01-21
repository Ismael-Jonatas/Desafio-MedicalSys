from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
]