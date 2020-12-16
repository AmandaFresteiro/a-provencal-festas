from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def cakes(request):
    return render(request, 'cakes.html')


def cakes_photo(request):
    return render(request, 'cakes-photo.html')


def party(request):
    return render(request, 'party.html')


def candy(request):
    return render(request, 'candy.html')


def about(request):
    return render(request, 'about.html')


def partykit(request):
    return render(request, 'partykit.html')


def start(request):
    return render(request, 'start.html')


