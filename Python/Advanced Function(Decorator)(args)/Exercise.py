##1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın. Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona
##1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

def mükemmel(fonk):
    def wrapper(sayılar):
        for i in sayılar:
            liste = []
            for j in range(1,i):
                if i % j == 0:
                    liste.append(j)

            if i == sum(liste):
                print(i)
        print("Mükemmel Sayılar: ")
        fonk(sayılar)
    return wrapper

@mükemmel
def asal(sayılar):
    print("Asal Sayılar: ")
    for i in sayılar:
        result = False
        for j in range(2,i):
            if result == True:
                break
            if i % j == 0:
                result = True
        if result == False:
            print(i)

asal(range(2,1000))


##def ekstra(fonk):
##    
##    def ekstra_ozellik():
##        print("Mükemmel Sayılar...")
##        for sayı in range(1,1001):
##            toplam = 0
##            i = 1
##            while (i < sayı):
##                if (sayı % i == 0):
##                    toplam += i
##                i +=1
##            if (toplam == sayı):
##                print(sayı)
##        fonk()
##                
##    return ekstra_ozellik
##    
##
##
##@ekstra
##def asal_sayılar():
##    print("Asal Sayılar...")
##    for sayı in range(2,1001):
##        i = 2 
##        say = 0
##        while (i < sayı):
##            if (sayı % i == 0):
##                say += 1
##            i += 1
##        if (say == 0):
##            print(sayı)
##            
##asal_sayılar()        
##    
