
# Create your views here.
from django.shortcuts import render, redirect
from .models import Donor, BloodBank, Request
from .forms import DonorForm, RequestForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})  # Return form with errors
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or any other page after login
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donors.html', {'donors': donors})

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()
    return render(request, 'add_donor.html', {'form': form})

def blood_stock(request):
    stock = BloodBank.objects.all()
    return render(request, 'stock.html', {'stock': stock})

def add_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_request')
    else:
        form = RequestForm()
    return render(request, 'add_request.html', {'form': form})

def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests.html', {'requests': requests})

def home(request):
    return render(request, 'home.html')