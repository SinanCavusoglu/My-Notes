import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()

def veri_ekle_input(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert Into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
#isim = input("İsim: ")
#yazar = input("Yazar: ")
#yayınevi = input("Yayınevi: ")
#sayfa_sayısı = int(input("Sayfa Sayısı: "))

#veri_ekle_input(isim,yazar,yayınevi,sayfa_sayısı)

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall() #list döner
    print(liste)
    print("""**********************
Tek Tek görmek için for i in liste kullan
************************""")
    for i in liste:
        print(i)

#verileri_al()

def verileri_al2():
    cursor.execute("Select İsim,Yazar From kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)


#verileri_al2()

def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print(liste)


# verileri_al3("TÜBİTAK")








con.close()
    
