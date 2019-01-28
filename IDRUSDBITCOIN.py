import requests
kode = input('ketikan nama bank:').lower()
url = 'https://kurs.web.id/api/v1/' + kode
data = requests.get(url)
Datakursbank = data.json()

url ='https://blockchain.info/tobtc?currency=USD&value=1'

dataBTC = requests.get(url)
dollarBTC = dataBTC.json()

if Datakursbank['error'] == "true":
    print('maaf data bank tidak tersedia')

else:
    jualbeli1 = input('Kurs yang mau diubah dari mana-kemana? (IDR-USD/USD-IDR)')
    if jualbeli1 != 'IDR-USD' or jualbeli1 != 'USD-IDR':
        print('wajib IDR-USD atau USD-IDR')
    else:
        totaltukar = int(input('mau di tuker berapa?'))
        kursbeli = int(Datakursbank['beli'])
        kursjual = int(Datakursbank['jual'])
        totalbeliUSD = totaltukar/kursbeli
        TotaljualIDR = totaltukar*kursjual
        # adollarBTC = int(dollarBTC)
        DolartoBTC = dollarBTC* int(totalbeliUSD)
        if jualbeli1 == 'IDR':
            print( str(totalbeliUSD) + 'USD-IDR')
            mauBTC = input('want to change to bitcoin? (yes/no)')
            if mauBTC == 'yes':
                print(DolartoBTC * totalbeliUSD)
            else:
                print('total diterima : ' + DolartoBTC + 'BTC')
        else:
            print( str(TotaljualIDR) + 'IDR-USD')
            mauBTC = input('want to change to bitcoin? (yes/no)')
            if mauBTC == 'yes':
                print(DolartoBTC * TotaljualIDR)
            else:
                print('total diterima : ' + str(TotaljualIDR) + 'USD')