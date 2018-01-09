from django.shortcuts import render
from django.template.loader import render_to_string
from .models import OtcNews, OtcSecurities

#need datetime to identify last 24 hours worth of news
from datetime import datetime, timedelta

#import modules useful for emailing
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

#OTC News View
def otcNewsList(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')[:100]
    return render(request, 'otcnews.html', {'newsItems': newsItems})

def otcSecuritiesList(request):
    securities = OtcSecurities.objects.all()
    return render(request, 'otcSecurities.html', {'securities': securities})

def sendNews(request):
    newsItems = OtcNews.objects.filter(category='news').order_by('-datetime')
    message = render_to_string('otcnewsEmail.html',{'newsItems': newsItems})
    send_mail("Last 24 hours of OTC News", "Here are the latest OTC news items:", 'jucharles91@gmail.com', ['jcharles18@gsb.columbia.edu'],html_message=message)
    #send_mail("Last 24 hours of OTC News", 'test', 'jucharles91@gmail.com', ['jcharles18@gsb.columbia.edu'])
    return HttpResponse("sent!")

