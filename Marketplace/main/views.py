from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required

def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})

def detalhes_produto(request, product_id):

    item = get_object_or_404(Item, id=product_id)
    return render(request, 'detalhes_produto.html', {'item': item})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Tentar autenticar o usuário
        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')  # Redireciona para a página inicial após o login
        else:
            return render(request, 'login.html', {'error_message': 'Email ou senha inválidos. Tente novamente.'})
    
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        last_name = request.POST.get('last_name', '')
        email = request.POST['email']
        telefone = request.POST['telefone']
        password = request.POST['password']

        try:
            # Criação do usuário
            user = User.objects.create_user(
                username=email,  # Aqui usamos o email como username
                first_name=username,
                last_name=last_name,
                email=email,
                password=password
            )

            # Autenticar e fazer login do usuário
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('index')  # Redireciona para a página inicial após o login
            else:
                return redirect('signup')

        except IntegrityError:
            return render(request, 'signup.html', {'error_message': 'Este email já está cadastrado. Tente outro.'})

    return render(request, 'signup.html')

def logout(request):
    auth_logout(request)
    return redirect('index')

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('index')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})