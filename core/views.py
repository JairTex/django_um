from multiprocessing import context

from requests import request

from .models import Produto
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse
from django.template import loader

def index(request):

    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        boas_vindas = 'Faça já o seu cadastro.'
    else:
        boas_vindas = f'Seja bem-vindo, {request.user}!'
    context = {
        'entrada' : boas_vindas,
        'curso' : 'Programação Web',
        'Outro' : 'Outro Conteudo',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk): 
    #prod = Produto.objects.get(id = pk)
    prod = get_object_or_404(Produto, id = pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type = 'text/html charset=utf8', status = 404)
    #return render(request, '404.html')

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type = 'text/html charset=utf8', status = 500)


