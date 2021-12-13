print("oyuncu kaydetme programı")

a=input("oyuncu ismi:")
b=input("oyuncu soyadı:")
c=input("oyuncu takımı:")

print("bilgiler kaydediliyor")

bilgiler=[a,b,c]

                  #formatın içine sadece liste olarak verilmiş değerleri yazabiliriz!
print("oyuncunun ismi:{}\n oyuncunun soyadı:{}\n oyuncunun takımı:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
print("bilgiler kaydedildi")