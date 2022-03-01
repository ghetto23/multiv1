from os import system as sys
from time import sleep

def clear():
    sys("clear")

def install(pack):
    sys("apt install {}".format(pack))

def wordlist(wd="/usr/share/wordlists/rockyou.txt"):
    wd = input("Wordlist yolunu belirtin(default rockyou.txt): ")
    return wd

x = "-"*20

def yazdir():
    print("\033[31m")
    clear()
    print("""
                                                            __       ______  
                                                            /  |     /      \ 
    ______    ______    _______  __    __         _______  _$$ |_   /$$$$$$  |
    /      \  /      \  /       |/  |  /  |       /       |/ $$   |  $$ |_ $$/ 
    /$$$$$$  | $$$$$$  |/$$$$$$$/ $$ |  $$ |      /$$$$$$$/ $$$$$$/   $$   |    
    $$    $$ | /    $$ |$$      \ $$ |  $$ |      $$ |        $$ | __ $$$$/     
    $$$$$$$$/ /$$$$$$$ | $$$$$$  |$$ \__$$ |      $$ \_____   $$ |/  |$$ |      
    $$       |$$    $$ |/     $$/ $$    $$ |      $$       |  $$  $$/ $$ |      
    $$$$$$$/  $$$$$$$/ $$$$$$$/   $$$$$$$ |       $$$$$$$/    $$$$/  $$/       
                                /  \__$$ |                                    
                                $$    $$/                                     
                                $$$$$$/                                     


    1) Port Scan
    2) HashIdentifier
    3) John
    4) Netcat 
    5) Steghide
    6) Stegcracker
    7) Exiftool

    """)

def main1():

    while True:
        try:    
            secim = int(input("Kullanacaginiz araci secin > "))
        except:
            print("TAM SAYI GIRINIZ!")
        else:
            break

    if secim == 1:
        print("""
        {}
        Nmap Port Tarama
        {}\n
        1) Default Scan
        2) Tum portlari tara
        3) Agresif Scan
    
        """.format(x,x))
        
        ded=int(input("Secim yapin > "))
        ip1=input("IP addressi girin > ")
        
        if ded == 1:
            sys("nmap -A -T4 -n -v {}".format(ip1))
        
        elif ded == 2:
            sys("nmap -T4 -p- -sS -sV {}".format(ip1))
        
        elif ded == 3:
            sys("nmap -A -n -sV {}".format(ip1))

        else:
            print("Yalnis secim!")

        
    elif secim == 2:
        hash1 = input("Hash degerini girin: ")
        sys("hash-identifier {}".format(hash1))

    elif secim == 3:
        clear()
        print(f"""
        {x*2}
        # CRACK HASH WITH JOHN THE RIPPER #
        {x*2}
        1. Hash turleri
        2. Hash BF (with rockyou.txt)
        3. Hash BF own wordlist
        99. Ana Menu
        """)

        a1 = int(input("\tSecim yapin > "))

        if a1 == 1:
            sys("john --list=formats")
        
        elif a1 == 2:
            print("NOT! Brute Force'da default olarak rockyou.txt kullanilacak.")
            b1 = input("Hash turunu belirtin: ")
            b2 = input("Hash bulunan dosya dizinini belirtin(ornek. /root/Desktop/hash.txt): ")
            sys("john --format={} {} --wordlist=/usr/share/wordlists/rockyou.txt".format(b1,b2))

        elif a1 == 3:
            c1 = input("Hash turunu belirtin: ")
            c2 = input("Hash bulunan dosya dizinini belirtin(ornek. /root/Desktop/hash.txt): ")
            c3 = input("Son olarak wordlist yolunu belirtin: ")
            sys("john --format={} {} --wordlist={}".format(b1,b2,b3))

        elif a1 == 99:
            main()

    elif secim == 4:
        clear()
        while True:
            try:
                port0=int(input("port numarasi girin > "))
            
            except:
                print("Lutfen dogru port numarasi yazin...")    

            else:
                break
        
        sys("nc -nvlp {}".format(port0))

    elif secim == 5:
        clear()
        install("steghide")
        clear()
        jpeg0 = input("Resim dosyasinin yolu: ")
        sys("steghide extract -sf {}".format(jpeg0))

    elif secim == 6:
        clear()
        install("stegcracker")
        clear()
        jpeg1 = input("resim dosyasi yolu: ")
        deds = wordlist()
        sys("stegcracker {} {}".format(jpeg1,deds))

    elif secim == 7:
        install("exiftool")
        clear()
        qw = input("resim yolu: ")
        sys("exiftool {}".format(qw))
        if not qw:
            clear()
            print("\nresim yolu belirtin!")
            sys("python3 easyctf.py")

    else:
        print("Yalnis secim ettiniz.")
        sleep(2)
        sys("python3 easyctf.py")

if __name__ == '__main__':
    yazdir()
    main1()
