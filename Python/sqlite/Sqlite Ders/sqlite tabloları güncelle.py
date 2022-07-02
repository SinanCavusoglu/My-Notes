import sqlite3

con = sqlite3.connect("kütüphane.db")
cursor = con.cursor()
## To remember
def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print(liste)
def veri_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()


def veri_güncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

##verileri_güncelle("GOA","CAN")
##verileri_göster()

def verileri_sil(yazar):
    cursor.execute("Delete From Kitaplık where Yazar = ?",(yazar,))
    con.commit()

##verileri_sil("Peyami Safa")

verileri_al()

con.close()
