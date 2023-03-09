import sqlite3 as sql

class functions:
    def __init__(self,username:str,password:str):
        self.username = username
        self.password = password

    def register(self):
        with sql.connect("database.db") as veritaban:
            imleç = veritaban.cursor()
            imleç.execute("""CREATE TABLE IF NOT EXISTS üyeler(kullanici_adi TEXT,şifre TEXT,para INT)""")
            imleç.execute("SELECT * FROM üyeler WHERE (kullanici_adi=? AND şifre=?)",(self.username,self.password))
            veri = imleç.fetchone()
            if veri:
                return "kullanici_zaten_var"
            elif not veri:
                imleç.execute("""INSERT INTO üyeler(kullanici_adi,şifre,para) VALUES (?,?,?)""",(self.username,self.password,0))
                return "kullanici_kayit_edildi"
                
    def login(self):
        with sql.connect("database.db") as veritaban:
            imleç = veritaban.cursor()
            imleç.execute("""CREATE TABLE IF NOT EXISTS üyeler(kullanici_adi TEXT,şifre TEXT,para INT)""")
            imleç.execute("""SELECT * FROM üyeler WHERE (kullanici_adi=? AND şifre=?)""",(self.username,self.password))
            veri = imleç.fetchone()

            if veri:
                return "giris_basarili"
            elif not veri:
                return "giris_basarisiz"

    