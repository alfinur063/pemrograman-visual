
import string
abjad = string.printable

def enkrip (pesan) :
    global abjad

    key = int (input('Masukkan key : '))
    Cipher=''
    for x in pesan :
            if x in abjad :
                a = abjad.find(x)
                a = (a + key)%100
                Cipher = Cipher + abjad[a]
            else :
                    Cipher = Cipher + x
                

    return Cipher


pesan = input('Masukkan Pesan : ')
print(enkrip(pesan))

