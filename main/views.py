from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def chifu(request):
    return render(request, 'chifu.html')

def contact(request):
    return render(request, 'contact.html')

def donar(request):
    return render(request, 'donar.html')

def login(request):
    return render(request, 'login.html')

def pacientes(request):
    return render(request, 'pacientes.html')

def perfil(request):
    return render(request, 'perfil.html')

def rayo(request):
    return render(request, 'rayo.html')

def signup(request):
    return render(request, 'sign up.html')

def winnie(request):
    return render(request, 'winnie.html')

def woody(request):
    return render(request, 'woody.html')