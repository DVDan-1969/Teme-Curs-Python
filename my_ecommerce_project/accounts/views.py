
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.user.is_authenticated:
        return redirect('shop:product_list')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Înregistrarea a fost realizată cu succes! Te poți loga acum.")
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('shop:product_list')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bun venit, {user.username}!")
                return redirect('shop:product_list')
        else:
            messages.error(request, "Nume utilizator sau parolă incorectă.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "Te-ai delogat cu succes.")
    return redirect('shop:product_list')

@login_required
def delete_user(request, user_id):
    # Verificăm dacă utilizatorul curent este superuser
    if not request.user.is_superuser:
        messages.error(request, "Nu ai permisiunea să faci asta!")
        return redirect('shop:product_list')  # sau orice altă pagină

    # Luăm user-ul de șters sau returnăm 404 dacă nu există
    user = get_object_or_404(User, id=user_id)

    # Prevenim ca superuser să-și șteargă propriul cont accidental
    if user == request.user:
        messages.error(request, "Nu poți să-ți ștergi propriul cont ca superuser!")
        return redirect('shop:product_list')

    user.delete()
    messages.success(request, f"User-ul {user.username} a fost șters cu succes.")
    return redirect('shop:product_list')
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

@login_required
def admin_view(request):
    if not request.user.is_superuser:
        messages.error(request, "Nu ai permisiunea să accesezi această pagină.")
        return redirect('shop:product_list')

    users = User.objects.all()
    return render(request, 'accounts/admin.html', {'users': users})
