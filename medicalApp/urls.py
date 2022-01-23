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
    path('paciente/<int:paciente_id>', views.crud_paciente, name='paciente'),
    path('agendamento/<int:agendamento_id>', views.crud_agendamento, name='agendamento'),
    path('deleta-paciente/<int:paciente_id>', views.deleta_paciente, name='deleta_paciente'),
    path('edita-paciente', views.edita_paciente, name='edita_paciente'),
    path('deleta-agendamento/<int:agendamento_id>', views.deleta_agendamento, name='deleta_agendamento'),
    path('edita-agendamento', views.edita_agendamento, name='edita_agendamento'),
    path('listar-usuarios', views.listar_usuario, name="listar_usuarios"),
    path('usuario/<int:usuario_id>', views.crud_usuario, name='usuario'),
    path('deleta-usuario/<int:usuario_id>', views.deleta_usuario, name='deleta_usuario'),
    path('edita-usuario', views.edita_usuario, name='edita_usuario'),


]