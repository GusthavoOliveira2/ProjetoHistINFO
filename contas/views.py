from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        user = request.user
        password = request.POST['password']
        user = authenticate(request, user=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecione para a página inicial ou outra
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos.'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecione para a página de login após logout
