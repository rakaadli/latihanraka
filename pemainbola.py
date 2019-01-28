
import requests

nama = input('Ketik klub bola: ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+nama
roleapa = input('mau cari untuk role apa: ')
roleapakapital = roleapa.capitalize()

data = requests.get(url)
output = data.json()

listpemain = data.json()['player']

for name in listpemain:
    if name['strPosition'] == roleapakapital:
        print(name['strPlayer'])
    else:
        pass