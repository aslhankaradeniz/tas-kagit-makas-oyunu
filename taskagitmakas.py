
oyuncu=input("oyuncu-1 ad: ")
oyuncu2=input("oyuncu-2 ad: ")
puan=0
puan2=0
while (True):
    a=input("%s lütfen taş,kağıt ve makas dan birini seçiniz: "%(oyuncu))
    b=input("%s lütfen taş,kağıt ve makas dan birini seçiniz: "%(oyuncu2))
    if a=="tas":
        if b=="tas":
            print("berabere")
        elif b=="makas":
            puan=puan+1
            print("%s kazandın"%(oyuncu),puan)
            
        elif b=="kagıt":
            puan2=puan2+1
            print("%s kazandın"%(oyuncu2),puan2)
            
    elif a=="kagıt":
        if b=="tas":
            puan=puan+1
            print("%s kazandın"%(oyuncu),puan)
            
        elif b=="kagıt":
            print("berabere")
        elif b=="makas":
            puan2=puan2+1
            print("%s kazandın"%(oyuncu2),puan2)
            
    elif a=="makas":
        if b=="tas":
            puan2=puan2+1
            print("%s kazandın"%(oyuncu2),puan2)
            
        elif b=="kagıt":
            puan=puan+1
            print("%s kazandın"%(oyuncu),puan)
            
        elif b=="makas":
             print("berabere")
    if puan==3 | puan2==3:
            break
if (puan==3):
        print(puan,"puan ile %s kazandı"%(oyuncu),puan)
elif (puan2==3):
        print(puan,"puan ile %s kazandı"%(oyuncu2),puan2)
else:
    print("yeniden deneyin")