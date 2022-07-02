import sys

##for i in range(1,5):
##    if i == 3 :
##        sys.exit()
##    print(i)
##
##    


##stderr ve stdout
##Bilgisayarlar uygulamalarımız ve işlemlerimiz çalıştığı zaman çıktı vermek ve girdi almak için şu dosyaları kullanır.
##
##stdin : Bu standard dosya, işlemimizin (process ) kullanıcıdan input almasını sağlar.
##
##stdout : Bu standard dosya, işlemimizin (process ) çıktı vermesini sağlar.
##
##stderr : Bu standard dosya, işlemimizin hata mesajlarını çıktı olarak vermek için kullanılır.
##
##Biz print() fonksiyonumuzu kullandığımızda aslında standard olarak stdout kullanılmaktadır.
##Ancak biz istersek *stderr'e de bir şeyler yazabiliriz.



##sys.stderr.write("Error Mesage\n") # write red
##
##sys.stdout.write("Normal Mesage\n") # write black(normal)
##


##print(sys.argv)

if len(sys.argv) > 1:
    print(float(sys.argv[1])+5)


## iki dil içinde kullanılıyor
