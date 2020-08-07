from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio_detail_page(request):
    return render(request, 'portfolio/portfolio.html')
