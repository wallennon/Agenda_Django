from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#redirecionando a página principal através da URL
# def index(request):
#     return redirect('/agenda/')


def lista_eventos(request):
    # para coletar o evento direto do usuário logado
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()  # aqui é passado todos os eventos listados no bd
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
