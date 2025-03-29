from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from .models import Wiki_pages

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

def feedback(request):
    if request.method == 'POST':
        email_address = request.POST.get('email')

        if email_address:
            email = Wiki_pages(title=email_address, description_path='wowwowwowwow')
            email.save()
            print(f"Получен email: {email}")
            return JsonResponse({'status': 'success', 'message': 'Email получен'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Email не получен'})
    return render(request, "index.html")

def wiki_page(request, wiki):
    wiki_page = get_object_or_404(Wiki_pages, pk = wiki)

def auth(request):
    body = json.loads(request.body)
    return render(request, 'account.html')