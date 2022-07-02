##Program 1
##"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir
##
##sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli
##bir tane parametre alsın ve her next işleminde ekrana üzerinde
##bulunduğunuz sayının karesi yazdırılsın.
##StopIteration hatası ekrana maksimum sayıyı geçtiğiniz zaman fırlatılsın.


class Kareler():

    def __init__(self,maksimum):

        self.maksimum = maksimum
        self.index = -1

    def __iter__(self):

        return self

    def __next__(self):

        self.index += 1
        if self.index <= self.maksimum :

            return self.index**2
        else:
            raise StopIteration
        

kareler = iter(Kareler(5))
print(next(kareler))
print(next(kareler))
print(next(kareler))
