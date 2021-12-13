#PROBLEM 6(Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.)

a=int(input("dik üçgenini birinci kısa kenarı:"))
b=int(input("dik üçgenin ikinci kısa kenarı:"))

hipotenüs=(a**2+b**2)**0.5

print(hipotenüs)