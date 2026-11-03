from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

# Create your views here.


def index(request):

    fotografias = Fotografia.objects.all()
    return render(request, 'Galeria/index.html',{"cards": fotografias} )

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'Galeria/imagem.html', {'fotografia': fotografia})
