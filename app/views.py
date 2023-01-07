from django.contrib.auth import authenticate
from django.core.checks import messages
from django.shortcuts import redirect, render

from app.forms import LoginForm
from app.models import Registration


def home(request):
    return render(request,'home.html')


def user_register(request):
    login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(request.POST, request.FILES)
        if login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()
            return redirect('home')
    return render(request,'user_register.html', {'login_form':login_form})


def user_view(request):
    data = Registration.objects.filter(is_user=True)
    return render(request, 'user_view.html', {'data': data})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_user:
                return redirect('user_view')

        else:
            messages.info(request, 'INVALID CREDENTIALS')
    return render(request, 'login.html')