from django.shortcuts import render

def index(request):
    return render(request, 'library/templates/index.html')  # nebo jiný šablonový soubor




