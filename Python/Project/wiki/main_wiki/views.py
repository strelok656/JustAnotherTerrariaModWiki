from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def account(request):
    return render(request, 'account.html')

def absorber(request):
    return render(request, 'Absorber.html')

def ash_slicer(request):
    return render(request, 'AshSlicer.html')

def cool_star(request):
    return render(request, 'CoolStar.html')

def blooming_crimtane(request):
    return render(request, 'BloomingCrimtane.html')