# from django.contrib.auth import login, logout
# from django.contrib.auth.context_processors import auth
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.models import User
# from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LandingPageView(View):
    def get(self, request):
        if 'keyword' in self.request:
            pass
        return render(request, 'index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
        return render(request, 'auth/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

