def ekstra(fonk):
    def wrapper(sayılar):
        tek_sayı_toplamı = 0
        tek_sayılar = 0
        çift_sayılar_toplamı = 0
        çift_sayılar = 0

        for i in sayılar:
            if i % 2 == 0:
                çift_sayılar_toplamı += i
                çift_sayılar += 1
            else:
                tek_sayı_toplamı += i
                tek_sayılar += 1
        print("Tek Sayıların Ortalaması",tek_sayı_toplamı/tek_sayılar)
        fonk(sayılar)
    return wrapper
        
@ekstra
def ortalamabul(sayılar):
    toplam = 0
    for i in sayılar:
        toplam += i

    print("Ortalama",toplam/len(sayılar))

    
ortalamabul(range(10))
