import os
from bs4 import BeautifulSoup as bsoup
import requests
url_my_city = 'https://meteofor.com.ua/weather-kyiv-4944/now/'
class_for_mycity = 'weather-value'

def Main():
    req = requests.get(url_my_city)
    html = bsoup(req.text, 'html.parser')
    myweather_temperature = html.find(class_=class_for_mycity).find(class_="temperature-value")
    print(myweather_temperature)

if __name__ == "__main__":
    Main()