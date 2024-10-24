from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Boleta, Payment
from .forms import RegisterForm, LoginForm, PaymentsForm
from django.contrib.auth.forms import AuthenticationForm
from datetime import datetime


# Create your views here.
def home(request):
    payments = Payment.objects.filter(user=request.user) if request.user.is_authenticated else None
    return render(request, 'core/index.html', {'payments': payments})

@login_required
def payment_list(request):
    selected_boleta = request.GET.get('boleta', '')
    mes = request.GET.get('mes')
    año = request.GET.get('año')
    pagado = request.GET.get('payed')

    payments = Payment.objects.filter(user=request.user)

    if selected_boleta:
        payments = payments.filter(boleta__id=selected_boleta) 

    if mes:
        payments = payments.filter(payment_due__month=int(mes))
    if año:
        payments = payments.filter(payment_due__year=int(año))
    if pagado:
        payments = payments.filter(payed=(pagado == '1'))  

    boletas = Boleta.objects.all()  

    meses = range(1, 13)
    años = range(2020, datetime.now().year + 1)

    return render(request, 'core/payment_list.html', {
        'payments': payments,
        'meses': meses,
        'años': años,
        'boletas': boletas,  
        'filtros': {'boleta': selected_boleta, 'mes': mes, 'año': año, 'payed': pagado},
    })




@login_required
def add_payment(request):
    if request.method == 'POST':
        form = PaymentsForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('core:payment_list')
    else:
        form = PaymentsForm()
    return render(request, 'core/add_payment.html', {'form': form})

@login_required
def edit_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id, user=request.user)
    if request.method == 'POST':
        form = PaymentsForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('core:payment_list')
    else:
        form = PaymentsForm(instance=payment)
    return render(request, 'core/edit_payment.html', {'form': form})
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            form.save()
            return redirect('/login/')
    else:
        form = RegisterForm() 

    return render(request, 'core/register.html', {
        'form': form
    })
    
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/') 
            else:
                form.add_error(None, "Credenciales incorrectas.")
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})
    
