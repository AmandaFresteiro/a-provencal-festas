from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def cakes(request):
    return render(request, 'cakes.html')


def party(request):
    return render(request, 'party.html')


def candy(request):
    return render(request, 'candy.html')


def about(request):
    return render(request, 'about.html')