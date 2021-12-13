#PROBLEM 1(Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.)
a=int(input("birinci sayi:"))
b=int(input("ikinci sayi:"))
c=int(input("ücüncü sayi:"))
d=a*b*c
print("{},{} ve {} sayılarının çarpımı {}'a eşittir.".format(a,b,c,d))
#format fonksiyonu tarzıyla yazmamızı istediği için mecburen çarpımlarını da bir değişkene atadık.

