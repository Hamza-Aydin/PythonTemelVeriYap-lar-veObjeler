#PROBLEM 2(Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.)

q=int(input("boy:"))
w=int(input("kilo:"))

bedenkitleindeksi=w/q**2
print(bedenkitleindeksi)