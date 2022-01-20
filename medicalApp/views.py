from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cadastro_usuario(request):
    return render(request, 'cadastro-usuario.html')

def login(request):
    return render(request, 'login.html')