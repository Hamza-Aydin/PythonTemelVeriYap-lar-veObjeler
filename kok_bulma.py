#iki bilinmeyenli denklemin köklerini bulma

#denklem=ax^2+bx+c

#deltayı hesaplama=b**2-4*a*c

#birinci kök=b**2 - delta**0.5 /(2*a)
#ikici kök=b**2+ delta**0.5 / (2*a)

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=b**2-4*a*c

kök1=(-b - delta**0.5) /(2*a)
kök2=(-b + delta**0.5) / (2*a)
#sayılarda format için tekrar listelemeye gerek yok !
print("birinci kök{}\n ikinci kök{}\n".format(kök1,kök2))


