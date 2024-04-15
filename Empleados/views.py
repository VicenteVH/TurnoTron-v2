from Clientes.forms import CreateUserForm, LoginForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from Clientes.models import BarberShop

def employee_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_employee:
                auth_login(request, user)
                return redirect('employee_dashboard')
            else:
                # Manejar error si el usuario no es un empleado
                pass
    else:
        form = LoginForm()
    return render(request, 'employee_login.html', {'form': form})

def employee_register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_employee = True
            user.save()
            barber_shop_id = request.POST.get('barber_shop')  # Obtener la barbería seleccionada
            if barber_shop_id:
                barber_shop = BarberShop.objects.get(pk=barber_shop_id)
                user.barber_shop = barber_shop
                user.save()
            return redirect('employee_login')
    else:
        form = CreateUserForm()
    return render(request, 'employee_register.html', {'form': form})
