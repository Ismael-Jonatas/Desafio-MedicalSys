from re import search
from django.contrib import admin
from .models import Usuario, Paciente, Agendamento

# Register your models here.

class Usuarios(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

class Pacientes(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('cidade',)
    list_per_page = 20
    
class Agendamentos(admin.ModelAdmin):
    list_display = ('id','data', 'status_agendamento', 'medico', 'paciente')
    list_display_links = ('id', 'data', 'status_agendamento', 'medico', 'paciente')
    search_fields = ('data',)
    list_filter = ('status_agendamento',)
    list_per_page = 20


admin.site.register(Usuario, Usuarios)
admin.site.register(Paciente, Pacientes)
admin.site.register(Agendamento, Agendamentos)