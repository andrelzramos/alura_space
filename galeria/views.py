from django.shortcuts import render

# Create your views here.


def index(request):

    dados = {
    1: {"nome": "Nebulosa de Carina",
        "legenda": "Webbtelecope.org / NASA / James Webb"},
    2: {"nome": "Galaxia NGC 1079",
        "legenda": "nasa.or / NASA / Hubble"}

    }

    return render(request, 'Galeria/index.html',{"cards": dados} )

def imagem(request):
    return render(request, 'Galeria/imagem.html')
