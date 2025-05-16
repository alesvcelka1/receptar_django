from django.shortcuts import render, get_object_or_404
from .models import Recept, Kuchar, Kategorie


def index(request):
    recepty = Recept.objects.all()
    return render(request, 'index.html', {'recepty': recepty})


def recepty_list(request):
    recepty = Recept.objects.all()
    return render(request, 'library/recepty_list.html', {'recepty': recepty})

def kuchari_list(request):
    kuchari = Kuchar.objects.all()
    return render(request, 'library/kuchari_list.html', {'kuchari': kuchari})

def kategorie_list(request):
    kategorie = Kategorie.objects.all()
    return render(request, 'library/kategorie_list.html', {'kategorie': kategorie})
def recept_detail(request, pk):
    recept = get_object_or_404(Recept, pk=pk)
    kategorie_id = request.GET.get('kategorie')

    predchozi = None
    dalsi = None
    zpet_url = None

    if kategorie_id:
        # Listování v rámci dané kategorie
        kategorie = get_object_or_404(Kategorie, pk=kategorie_id)
        zpet_url = f"/kategorie/{kategorie_id}/"  # Pro tlačítko zpět

        recepty = Recept.objects.filter(kategorie=kategorie).order_by('id').distinct()
        recept_ids = list(recepty.values_list('id', flat=True))
        current_index = recept_ids.index(recept.id)

        if current_index > 0:
            predchozi = Recept.objects.get(pk=recept_ids[current_index - 1])
        if current_index < len(recept_ids) - 1:
            dalsi = Recept.objects.get(pk=recept_ids[current_index + 1])
    else:
        # Globální listování (pokud není filtr kategorie)
        recepty = Recept.objects.all().order_by('id')
        recept_ids = list(recepty.values_list('id', flat=True))
        current_index = recept_ids.index(recept.id)

        if current_index > 0:
            predchozi = Recept.objects.get(pk=recept_ids[current_index - 1])
        if current_index < len(recept_ids) - 1:
            dalsi = Recept.objects.get(pk=recept_ids[current_index + 1])

    return render(request, 'library/recept_detail.html', {
        'recept': recept,
        'predchozi': predchozi,
        'dalsi': dalsi,
        'zpet_url': zpet_url
    })

def kategorie_detail(request, pk):
    kategorie = get_object_or_404(Kategorie, pk=pk)
    recepty = Recept.objects.filter(kategorie=kategorie)
    return render(request, 'library/kategorie_detail.html', {
        'kategorie': kategorie,
        'recepty': recepty
    })
def kuchar_detail(request, pk):
    kuchar = get_object_or_404(Kuchar, pk=pk)
    recepty = Recept.objects.filter(kuchar=kuchar)
    return render(request, 'library/kuchar_detail.html', {
        'kuchar': kuchar,
        'recepty': recepty
    })