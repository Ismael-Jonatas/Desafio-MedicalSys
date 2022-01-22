from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth

from .models import Paciente, Usuario

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastro_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']


        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro_usuario')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro_usuario')
        if Usuario.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro_usuario')

        user = Usuario.objects.create(nome=nome, email=email, senha=senha)
        user.save()
        print('cadastrado')
        return redirect('login')
    else:
         return render(request, 'cadastro-usuario.html')


def cadastro_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        CEP = request.POST['cep']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        UF = request.POST['uf']
        pais = request.POST['pais']

        if not nome.strip():
            print('O campo nome não pode está em branco')
            redirect('cadastro_paciente')
        if not endereco.strip():
            print('O campo endereço não pode está em branco')
            redirect('cadastro_paciente')
        if not cidade.strip():
            print('O campo cidade não pode está em branco')
            redirect('cadastro_paciente')
        if not UF.strip():
            print('O campo UF não pode está em branco')
            redirect('cadastro_paciente')
        if not pais.strip():
            print('O campo pais não pode está em branco')
            redirect('cadastro_paciente')

        paciente = Paciente.objects.create(nome=nome,telefone=telefone,CEP=CEP,endereco=endereco,cidade=cidade,UF=UF,pais=pais)
        paciente.save()
        print('cadastrado Paciente '+nome)
        return redirect('listar_pacientes')
    else:    
        return render(request, 'cadastro-paciente.html')


def listar_pacientes(request):
    pacientes = Paciente.objects.all().order_by('id')
    for paciente in pacientes:
        paciente.data_criacao = paciente.data_criacao.strftime("%b %d, %Y")
    dados = {
        'pacientes': pacientes
    }
    return render (request, 'listar-paciente.html',dados)

def crud_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk = paciente_id)
    exibir_paciente = {
        'paciente':paciente
    }
    return render(request, 'paciente.html', exibir_paciente)




def login(request):
    if request.method == 'POST':
        
        m = Usuario.objects.get(email=request.POST['email'])
        if m.senha == request.POST['senha']:
            request.session['member_id'] = m.id
            request.session.set_expiry(1500)
            return redirect('listar_pacientes')
        else:
            print('Usuario inexistente')
            return redirect('cadastro_usuario')   
    else:
        return render(request, 'login.html')


def logout (request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return redirect('index')