from django.shortcuts import render
from .models import Pet

def home(request):
    return render(request, 'pet/index.html')
