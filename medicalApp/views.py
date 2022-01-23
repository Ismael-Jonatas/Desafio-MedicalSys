from re import S
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
        if not senha.strip():
            messages.error(request, 'O campo senha não pode ficar em branco')
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


def listar_usuario(request):
    usuarios = Usuario.objects.all().order_by('id')
    for usuario in usuarios:
        usuario.data_criacao = usuario.data_criacao.strftime("%b %d, %Y")
    dados = {
        'usuarios': usuarios
    }
    return render (request, 'listar-usuario.html',dados)


def crud_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk = usuario_id)
    exibir_usuario = {
        'usuario':usuario
    }
    return render(request, 'usuario.html', exibir_usuario)


def deleta_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    usuario.delete()
    messages.warning(request,'Paciente deletado com sucesso')
    return redirect('listar_usuarios')


def edita_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        usuario_senha = request.POST['usuario_senha']
        print('senha atual no banco: '+usuario_senha)
        senha = request.POST['senha']
        print('senha atual a ser verificada: '+senha)
        senha2 = request.POST['senha2']
        print('nova senha: '+senha2)
        senha3 = request.POST['senha3']
        print('comfirmação de nova senha: '+senha3)


        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('listar_usuarios')
        if not senha.strip() or not senha2.strip():
            messages.error(request, 'O campo senha não pode ficar em branco')
            return redirect('listar_usuarios')
        if senha != usuario_senha:
            messages.error(request, 'Essa não é sua senha atual!')
            return redirect('listar_usuarios')
        if senha == senha2:
            messages.error(request, 'A nova senha não pode ser igual à atual')
            return redirect('listar_usuarios')
        if senha2 != senha3:
            messages.error(request, 'As novas senhas não são iguais')
            return redirect('listar_usuarios')
        
        usuario_id = request.POST['usuario_id']
        usuario = Usuario.objects.get(pk=usuario_id)

        if Usuario.objects.filter(email=email).exists():
            if usuario.email == email:
                usuario.nome = nome
                usuario.senha = senha2

                usuario.save()
                messages.info(request, 'Usuário atualizado com sucesso')
                return redirect('listar_usuarios')
            
            else:

                messages.error(request, 'Este email já está vinculado a outro usuário')
                return redirect('listar_usuarios')

        usuario.nome = nome
        usuario.email = email
        usuario.senha = senha2

        usuario.save()
        messages.info(request, 'Usuário atualizado com sucesso')
        return redirect('listar_usuarios')

    return redirect('listar_usuarios')


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
            return redirect('cadastro_paciente')
        if not endereco.strip():
            messages.error(request, 'O campo endereço não pode ficar em branco')
            return redirect('cadastro_paciente')
        if not cidade.strip():
            messages.error(request, 'O campo cidade não pode ficar em branco')
            return redirect('cadastro_paciente')
        if not uf.strip():
            messages.error(request, 'O campo UF não pode ficar em branco')
            return redirect('cadastro_paciente')
        if not pais.strip():
            messages.error(request, 'O campo Pais não pode ficar em branco')
            return redirect('cadastro_paciente')

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


def edita_paciente(request):
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
            return redirect('listar_pacientes')
        if not endereco.strip():
            messages.error(request, 'O campo endereço não pode ficar em branco')
            return redirect('listar_pacientes')
        if not cidade.strip():
            messages.error(request, 'O campo cidade não pode ficar em branco')
            return redirect('listar_pacientes')
        if not uf.strip():
            messages.error(request, 'O campo UF não pode ficar em branco')
            return redirect('listar_pacientes')
        if not pais.strip():
            messages.error(request, 'O campo Pais não pode ficar em branco')
            return redirect('listar_pacientes')

        paciente_id = request.POST['paciente_id']
        paciente = Paciente.objects.get(pk=paciente_id)
        paciente.nome = nome
        paciente.telefone = telefone
        paciente.CEP = cep
        paciente.endereco = endereco
        paciente.cidade = cidade
        paciente.UF = uf
        paciente.pais = pais

        paciente.save()
        messages.info(request,'Paciente editado com sucesso')
        return redirect('listar_pacientes')
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
    
    agendamento = []
    agendamento = get_object_or_404(Agendamento, pk = agendamento_id)
    pacientes = []
    pacientes = Paciente.objects.all().order_by('id')
    usuarios = []
    usuarios = Usuario.objects.all().order_by('id')

    return render(request, 'agendamento.html', {'agendamento':agendamento, 'lista_usuarios':usuarios, 'lista_pacientes':pacientes})


def deleta_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    agendamento.delete()
    messages.warning(request,'Agendamento deletado com sucesso')
    return redirect('listar_agendamentos')


def edita_agendamento(request):
    if request.method == 'POST':
        medico = request.POST['medico']
        paciente = request.POST['paciente']
        status = request.POST['status']
        descricao = request.POST['descricao']
        data = request.POST['data']

        if not descricao.strip():
            messages.error(request, 'O campo descricao não pode ficar em branco')
            return redirect('listar_agendamentos')

        agendamento_id = request.POST['agendamento_id']
        agendamento = Agendamento.objects.get(pk=agendamento_id)
        agendamento.medico_id = medico
        agendamento.paciente_id = paciente
        agendamento.status_agendamento = status
        agendamento.descricao = descricao
        agendamento.data = data

        agendamento.save()
        messages.info(request,'Agendamento editado com sucesso')
        return redirect('listar_agendamentos')
    
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