from django.shortcuts import render, get_object_or_404
# Create your views here.
from contact.models import Grupi, Kompanija, Lice

def index(request):
    lista_grupi = Grupi.objects.all().order_by('datum_kreiranje')[:5]
    context = {'lista_grupi' : lista_grupi}
    return render(request, 'index.html', context)

def kompanii(request, grupa_id):
    grupi = get_object_or_404(Grupi, pk=grupa_id)
    return render(request, 'kompanii.html', {'grupi' : grupi})

def lica(request, grupa_id):
    kompanija = get_object_or_404(Kompanija, pk=grupa_id)
    return render(request, 'lica.html', {'kompanija' : kompanija})

