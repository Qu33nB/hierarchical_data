from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from data_app.models import CustomUser
from data_app.forms import SignInForm, SignUpForm

# Create your views here.
@login_required
def index(request):
    html = 'index.htm'
    return render(request, 'index.htm')

def signin(request):
    html = 'generic_form.htm'
    
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = SignInForm()
    return render(request, html, {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signup(request):
    html = 'generic_form.htm'

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                homepage=data['homepage']
                )
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()
    return render(request, html, {'form': form})
