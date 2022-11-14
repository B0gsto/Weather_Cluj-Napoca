from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


# Create your views here.
def get_weather(response):
    # Fetch the page and create a Beautiful Soup object
    page = requests.get(
        "https://weather.com/weather/today/l/00b19086e498ac9d9e26c6a1017cf50e56904513548a563fb2839cf6a66bf3e6").text
    soup = BeautifulSoup(page, "html.parser")
    # Locate every div tags that has class name of "quote"
    temp = int(soup.find(class_="CurrentConditions--tempValue--MHmYY").contents[0][:-1])
    ctemp = (temp - 32) * 5 / 9
    final_temp = '%.2f' % ctemp
    print()
    #return HttpResponse(final_temp + '°Celsius ' + 'in Cluj-Napoca')
    return render(response, 'index.html', {'temp': final_temp})
