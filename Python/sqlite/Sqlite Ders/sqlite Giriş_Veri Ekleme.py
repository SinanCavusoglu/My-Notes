import sqlite3

# Connection oluştur
con = sqlite3.connect("kütüphane.db")
# Cursor(imleç) oluştur
cursor = con.cursor()



# Tablo oluşturalım

#CREATE TABLE kitaplık(isim TEXT, Yazar TEXT, YAYINEVİ TEXT, Sayfa sayısı int)
# Eğer iki kere kullanırsan Tablo Already Exist hatası alırız.

#CREATE TABLE IF NOT EXISTS kitaplık(isim TEXT, Yazar TEXT, YAYINEVİ TEXT, Sayfa sayısı int)
# Bu sorgu tablo var ise oluşturacak iki kere kullanırsan hata vermeyecek


def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT, Sayfa_Sayısı INT)" )
    con.commit()

#!!!! tablo_olustur() dersek tablo oluşturur!

# Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.


def veri_ekle():
    cursor.execute("Insert into kitaplık Values('İstanbul Hatırası','Ahmet Ümit','Everest',561)")
    con.commit()

#!!!!veri_ekle()



def veri_ekle_input(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert Into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
#isim = input("İsim: ")
#yazar = input("Yazar: ")
#yayınevi = input("Yayınevi: ")
#sayfa_sayısı = input("Sayfa Sayısı: ")
#veri_ekle_input(isim,yazar,yayınevi,sayfa_sayısı)


#File gibi kapatmamız lazım
con.close()
