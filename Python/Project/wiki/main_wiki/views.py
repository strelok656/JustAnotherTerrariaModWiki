from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Wiki_pages

def index(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'index.html', context)

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

def wiki_page(request, wiki):
    wiki_page = get_object_or_404(Wiki_pages, pk = wiki)

def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'login: {username}, password: {password}')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return JsonResponse({'status': 'error', 'message': 'Неверный логин и/или пароль'})
    return render(request, 'account.html')

def reg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = User.objects.create_user(username, email, password)
        user.first_name = name
        user.last_name = last_name
        user.save()
        login(request, user)
        context = {'name' : name}
        return render(request, "index.html", context)
    
    return render(request, 'reg.html')