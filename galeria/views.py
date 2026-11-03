from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Galeria/index.html')

def imagem(request):
    return render(request, 'Galeria/imagem.html')
