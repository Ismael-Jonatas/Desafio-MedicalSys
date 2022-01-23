from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar-usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('cadastrar-paciente', views.cadastro_paciente, name='cadastro_paciente'),
    path('cadastrar-agendamento', views.cadastro_agendamento, name='cadastro_agendamento'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('listar-pacientes', views.listar_pacientes, name='listar_pacientes'),
    path('listar-agendamentos', views.listar_agendamentos, name='listar_agendamentos' ),
    path('listar/<int:paciente_id>', views.crud_paciente, name='paciente'),
    path('agendamento/<int:agendamento_id>', views.crud_agendamento, name='agendamento')
]