from django.shortcuts import render
from .services import fetch_magnet
from django.http import JsonResponse

def ui(request):
    return render(request, "nyaa_extractor/ui.html")

def get_magnets(request):
    query = request.GET.get('query')
    if query:
        search_url = f"https://sukebei.nyaa.si/?f=0&c=0_0&q={query}"
        magnets = fetch_magnet.call(search_url)
        return JsonResponse({"magnets": magnets})
    else:
        return JsonResponse({"magnets": []})