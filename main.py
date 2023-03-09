from modules.functions import *
from colorama import Back, Fore
from time import sleep
import sqlite3
import os

while True:

    komutlar = ["?yardım","?giris","?kayit","?temizle","?cikis"]

    işlem = input(Fore.GREEN + "zCurq_bank:~$ " + Fore.RESET)

    if işlem in komutlar:
        if işlem == "?yardım":
            print("===[" +  Fore.MAGENTA + "zCurq Bank yardım paneli" + Fore.RESET + "]===")
            print(Fore.CYAN + "?kayit" + Fore.RESET + " = Banka sistemine kayıt olmani sağlar.")
            print(Fore.CYAN + "?giris" + Fore.RESET + " = Banka sistemine giriş yapmanı sağlar.")
            print(Fore.CYAN + "?temizle" + Fore.RESET + " = Terminali temizler.")
            print(Fore.CYAN + "?cikis" + Fore.RESET + " = Sistemden çıkar.")

        elif işlem == "?temizle":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        elif işlem == "?cikis":
            exit()

        elif işlem == "?kayit":
            kullanici = input(Fore.LIGHTCYAN_EX + "Kullanıcı adınızı girin" + Fore.RESET + "\n>")
            şifre = input(Fore.LIGHTCYAN_EX + "Şifrenizi girin" + Fore.RESET + "\n>")

            kayit = functions(kullanici,şifre)
            durum = kayit.register()

            if durum == "kullanici_zaten_var":
                print(Fore.RED + kullanici + Fore.RESET + " zaten sisteme kayıtlı.")
            elif durum == "kullanici_kayit_edildi":
                print(Fore.GREEN + kullanici + Fore.RESET + " sisteme başarı ile kayıt edildi.\n" + Fore.BLUE + "?giris" + Fore.RESET + " ile giriş yapabilirsiniz.")
            else:
                pass

        elif işlem == "?giris":
            kullanici = input(Fore.LIGHTCYAN_EX + "Kullanıcı adınızı girin" + Fore.RESET + "\n>")
            şifre = input(Fore.LIGHTCYAN_EX + "Şifrenizi girin" + Fore.RESET + "\n>")
            
            giris = functions(kullanici,şifre)
            durum = giris.login()

            if durum == "giris_basarili":
                print(Back.GREEN + "Giriş başarılı bilgileriniz aşağıda yer alıyor." + Back.RESET)

                with sqlite3.connect("database.db") as vt:
                    im = vt.cursor()

                    im.execute("""SELECT * FROM üyeler WHERE (kullanici_adi=? AND şifre=?)""",(kullanici,şifre))
                    veri = im.fetchone()

                    print(Fore.LIGHTMAGENTA_EX + "Para: " + Fore.RESET + str(veri[2]))


    else:
        print(Fore.RED + str(işlem) + Fore.RESET + " geçerli bir komut değil. " + "Geçerli komutlar için " + Fore.GREEN + "?yardım" + Fore.RESET +" yazınız.")
        sleep(0.6)


