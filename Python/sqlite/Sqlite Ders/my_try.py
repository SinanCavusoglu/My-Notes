import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def veri_yaz(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert Into kitaplık Values (?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

    
##while True:
##    isim = input("isim: ")
##    yazar = input("yazar: ")
##    yayınevi = input("yayınevi: ")
##    sayfa_sayısı = int(input("sayfa sayısı: "))
##    veri_yaz(isim,yazar,yayınevi,sayfa_sayısı)
##    control = input("iptal i yada herhangi bir şey")
##    if control == "i":
##        break

def veri_ver():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)

veri_ver()

##def veri_değiştir(değişen,değiştirilen):
##    cursor.execute("Update kitaplık set Yazar = ? where Yazar = ?",(değişen,değiştirilen))
##    con.commit()
##veri_değiştir("Jose Mauro De Vasconceloso","Jose Mauro")
    
con.close()
