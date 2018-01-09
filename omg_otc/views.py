from django.shortcuts import render
from otcNews.models import OtcNews, OtcSecurities

def home(request):
    return render(request,'home.html')

def search(request):
    q = request.GET.get('q')
    newsItems = OtcNews.objects.filter(ticker=q)
    return render(request, 'otcnews.html', {'newsItems': newsItems})
