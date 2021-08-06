from django.shortcuts import render
import requests
import time

# Create your views here.
def get_html_content(city):

    city=city.replace(' ','+')
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content=session.get(f"https://www.google.com/search?q={city}+weather").text
    return html_content

def home(request):
    weatherData=dict()
    if 'city' in request.GET:
        city=request.GET.get('city')
        result=get_html_content(city)
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(result,'html.parser')
        weatherData=dict()
        weatherData['region']= soup.find("span", class_ = 'BNeawe tAd8D AP7Wnd').text
        weatherData['temp']= soup.find("div", class_ = 'BNeawe iBp4i AP7Wnd').text
        # = soup.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text
        weatherData['status'],weatherData['dayHour']= soup.find("div", class_ = 'BNeawe tAd8D AP7Wnd').text.split('\n')
        print(weatherData['dayHour'])
        print(weatherData['temp'])
        print(weatherData['region'])
        print(weatherData['status'])
        # weatherData['time']=soup.find("div",attrs={"id":"wob_dts"}).text
        # weatherData['temp']=soup.find("span",attrs={"id":"wob_tm"}).text
        # weatherData['status']=soup.find("span",attrs={"id":"wob_dc"}).text
        # weatherData['wind']=soup.find("span",attrs={"id":"wob_ws"}).text
        # weatherData['humidity']=soup.find("span",attrs={"id":"wob_hm"}).text
    return render(request, 'weather/index.html',{'data':weatherData})
