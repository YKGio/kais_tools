from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.apps import apps
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    apps_list = [
        ('Nyaa Extractor', '/nyaa_extractor/'),
    ]
    return render(request, 'home.html', locals())

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        next_url = request.POST.get('next', '/')
        return redirect(next_url)
    else:
        next_url = request.GET.get('next', '/')  # 默認重定向到首頁
        return render(request, 'login.html', {'next': next_url})
    

def logout(request):
    auth.logout(request)
    return redirect('home')