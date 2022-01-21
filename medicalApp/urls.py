from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listar-pacientes', views.listar_pacientes, name='listar_pacientes'),
    path('cadastro-paciente', views.cadastro_paciente, name='cadastro_paciente'),
    path('<int:paciente_id>', views.crud_paciente, name='paciente')
]