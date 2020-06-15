from django.shortcuts import render
from data_app.models import Data
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    html = 'index.htm'
    data = Data.objects.all()
    return render(request, html, {'data': data})
