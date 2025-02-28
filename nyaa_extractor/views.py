from django.shortcuts import render
from .services import fetch_magnet
from django.http import JsonResponse as JasonResponse

# Create your views here.

def ui(request):
    return render(request, "ui.html")

def get_magnets(request):
    query = request.GET.get('query')
    search_url = f"https://sukebei.nyaa.si/?f=0&c=0_0&q={query}"
    if search_url:
        magnets = fetch_magnet.call(search_url)
        return JasonResponse({"magnets": magnets})
    else:
        return JasonResponse({"magnets": []})