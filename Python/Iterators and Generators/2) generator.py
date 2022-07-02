## range fonksiyonu aslında generator
def kareleri_al():
    for i in range(1,4):
        yield i**2

generator = kareleri_al()
print(generator)
##<generator object kareleri_al at 0x0000021689B82FF0>

iterator = iter(generator)
print(next(iterator))
## 1

print(next(iterator))
## 4

## 1 and 4 not occupy any memory

iterator2 = iter(generator)

print(next(iterator2))
## 9  görüldüğü gibi yeni bir değişkene atasak bile diğer değerler yok oldu


liste = [i * 3 for i in range(5)]

generator = (i * 3 for i in range(5))

print(generator)
## <generator object <genexpr> at 0x0000029175C63B50>


for i in generator:
    print(i)
##0
##3
##6
##9
##12

print(next(generator))
##StopIteration

