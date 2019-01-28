print('Selamat datang')
print('Silahkan pilih program yang akan Anda mau :')
print(' (1) KODE MORSE')
print(' (2) IDR USD BITCOIN')
print(' (3) CUACA')
print(' (4) Pemain Bola')

try:
    pilihanprogram = int(input('Input program yang kamu mau (1/2/3): '))
except ValueError:
    print('coba lagi pakai angka')
except NameError:
    print('coba lagi pakai angka jangan huruf')

if pilihanprogram == int(1):

    import morse

    # morse.ubah(input('ketikan kalimat untuk diubah = '))\\

    play = True
    play1 = True
    while play:
        try: 
            morse.ubah(input('ketikan kalimat untuk diubah = '))
            play1 = True
        except ValueError:
            print('tidak ada dalam list morse')
        except KeyboardInterrupt:
            print('KETIK YANG BENER WOOY')
        while play1:
            again=str(input("Do you want to translate, type yes or no : "))
            if again != "no" and again != "yes":
                print('ketik yes or no aja yaa')
                play1 = True
            elif again == "no":
                play = False
                play1 = False
            elif again == "yes":
                play1 = False
                play = True

elif pilihanprogram == int(2):
    import IDRUSDBITCOIN

elif pilihanprogram == int(3):
    import cuaca

elif pilihanprogram == int(4):
    import pemainbola