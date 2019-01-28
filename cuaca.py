
import requests

try:
    cari = input('nama kota:')
except ValueError:
    print('nama kota tidak tersedia')

appid = 'e48a7eddac52ba45d036c66ae136f14c'
url = 'http://api.openweathermap.org/data/2.5/weather?q='


data = requests.get(url+cari+'&APPID=' +appid)

print(data.json()['weather'][0]['main'])