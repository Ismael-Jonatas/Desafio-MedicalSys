from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import auth, messages
from .models import Agendamento, Paciente, Usuario

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
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro_usuario')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro_usuario')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('cadastro_usuario')

        user = Usuario.objects.create(nome=nome, email=email, senha=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    
    return render(request, 'cadastro-usuario.html')


def cadastro_paciente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        telefone = request.POST['telefone']
        cep = request.POST['cep']
        endereco = request.POST['endereco']
        cidade = request.POST['cidade']
        uf = request.POST['uf']
        pais = request.POST['pais']

        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            redirect('cadastro_paciente')
        if not endereco.strip():
            messages.error(request, 'O campo endereço não pode ficar em branco')
            redirect('cadastro_paciente')
        if not cidade.strip():
            messages.error(request, 'O campo cidade não pode ficar em branco')
            redirect('cadastro_paciente')
        if not uf.strip():
            messages.error(request, 'O campo UF não pode ficar em branco')
            redirect('cadastro_paciente')
        if not pais.strip():
            messages.error(request, 'O campo Pais não pode ficar em branco')
            redirect('cadastro_paciente')

        paciente = Paciente.objects.create(nome=nome,telefone=telefone,CEP=cep,endereco=endereco,cidade=cidade,UF=uf,pais=pais)
        paciente.save()
        messages.success(request, 'Paciente cadastrado com sucesso')
        return redirect('listar_pacientes')
       
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


def deleta_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.delete()
    messages.warning(request,'Paciente deletado com sucesso')
    return redirect('listar_pacientes')


def cadastro_agendamento(request):
    if request.method == 'POST':
        medico = request.POST['medico']
        paciente = request.POST['paciente']
        status = request.POST['status']
        descricao = request.POST['descricao']
        data = request.POST['data']

        if not descricao.strip():
            messages.error(request, 'O campo descricao não pode ficar em branco')
            return redirect('cadastro_agendamento')
        
        agendado = Agendamento.objects.create(status_agendamento=status, data=data, descricao=descricao, medico_id = medico, paciente_id = paciente)
        agendado.save()
        messages.success(request, 'Agendamento cadastrado com sucesso')
        return redirect('listar_agendamentos')
                

    pacientes = []
    pacientes = Paciente.objects.all().order_by('id')
    usuarios = []
    usuarios = Usuario.objects.all().order_by('id')

    return render(request, 'cadastro-agendamento.html', {'lista_usuarios':usuarios, 'lista_pacientes':pacientes})


def listar_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('id').filter()
    dados = {
        'agendamentos':agendamentos
    }

    return render(request, 'listar-agendamento.html', dados)


def crud_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk = agendamento_id)
    exibir_agendamento = {
        'agendamento': agendamento
    }
    return render(request, 'agendamento.html', exibir_agendamento)


def deleta_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Paciente, pk=agendamento_id)
    agendamento.delete()
    messages.warning(request,'Agendamento deletado com sucesso')
    return redirect('listar_agendamentos')





def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        senha = request.POST['senha']
        if Usuario.objects.filter(email=email).exists():
            user = Usuario.objects.get(email=email)
            nome = Usuario.objects.filter(email=email).values_list('nome', flat=True).get() 
            if user.senha == senha:
                request.session['member_id'] = user.id
                request.session.set_expiry(1500)
                messages.success(request, 'Logado com sucesso')
                return redirect('listar_pacientes')
            else:
                messages.error(request, 'Senha incorreta')        
                return redirect('login')
        else:
            messages.error(request, 'Email não cadastrado')
            return redirect('cadastro_usuario')   
    
    return render(request, 'login.html')


def logout (request):
    try:
        del request.session['member_id']
        messages.success(request, 'Logout efetuado com sucesso')
    except KeyError:
        pass
    return redirect('index')