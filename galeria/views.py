from django.shortcuts import get_object_or_404, render
from galeria.models import Fotografia


def index(request):
    fotografia = Fotografia.objects.order_by("date_fotografia").filter(visible=True)

    return render(request, 'galeria/index.html', {"cards":fotografia})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})