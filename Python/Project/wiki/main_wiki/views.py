from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Wiki_pages

def index(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'index.html', context)

def account(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'account.html', context)

def absorber(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'Absorber.html', context)

def ash_slicer(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'AshSlicer.html', context)

def cool_star(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'CoolStar.html', context)

def blooming_crimtane(request):
    name = request.user.username
    context = {'name' : name}
    return render(request, 'BloomingCrimtane.html', context)

def wiki_page(request, wiki):
    wiki_page = get_object_or_404(Wiki_pages, pk = wiki)

def account(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            print(f'login: {username}, password: {password}')
            return JsonResponse({'status': 'success', 'message': 'OK'})
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
        print(f"New account: {username}, {password}")
        return JsonResponse({'status': 'success', 'message': 'Регистрация прошла успешно'})
    
    return render(request, 'reg.html')

def acc(request):
    try:
        context = {
            'username': request.user.username,
            'name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'date_joined': request.user.date_joined
        }

        return render(request, "acc.html", context)
    except AttributeError as e:
        return render(request, "acc.html")

@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout_state = request.POST.get("logout")
        if logout_state:
            logout(request)
            return JsonResponse({'status': 'success', 'message': 'Выход из аккаунта успешен'})