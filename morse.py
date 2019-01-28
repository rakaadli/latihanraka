morse = {
    'a' : '.-',
    'b' : '-...',
    'c' : '-.-.',
    'd' : '-..',
    'e': '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '....',
    'i' : '..',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm': '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.--.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-', 
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..',
    '.' : '.-.-',
    ',' : '--..--',
    '?' : '..--..',
    '/' : '--..-.',
    '@' : '.--.-.',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    '0' : '-----',
}

# def ubahkemorse(teks):
    # kata = teks.lower().replace(' ','')
    # hasil =''
    # for i in kata:
    #     hasil += morse[i] + '/'
    # print(hasil)

# def ubahkekata(teks):
#     kalimat = teks.split('/')
#     hasil = ''
#     for i in kalimat:
#         hasil += list(morse.keys())[list(morse.values()).index(i)]
#     print(hasil)




def ubah(teks):
        if teks.lower() != teks.upper():
            kata = teks.lower().replace(' ','')
            hasil =''
            for i in kata:
                hasil += morse[i] + '/'
            print(hasil)
        else:
            kalimat = teks.split('/')
            hasil = ''
            for i in kalimat:
                hasil += list(morse.keys())[list(morse.values()).index(i)]
            print(hasil)
            
            



# ubahkemorse(input('ketikan kalimat untuk diubah ke morse = '))
# ubahkekata(input('ketikan kalimat untuk diubah ke kata = '))
# ubah(input('ketikan kalimat untuk diubah = '))

