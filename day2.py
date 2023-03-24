faiz=1.59
vade="36"
krediAdi="İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade)+12)
# print(int(krediAdi))
faiz=str(faiz)
print(type(faiz))

vade=36  #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade=vade+12

#string interpolation
# metinsel ifadelerin dinamikleştirilmesi
#seçtiğiniz vade sonucu ortaya çıkan vade:
print("Seçtiğiniz vade sonucu ortaya çıkan vade: "+str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade)) #format
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}") #f-string

isim="Halit" #input("isim giriniz")
metin="Merhaba {name}".format(name=isim)
print(metin)

# f-string
metin=f"Hoşgeldiniz{1+1}"
print(metin)

#listeler
#döngüler
#fonksiyonlar


dizi=["İhtiyaç Kredisi", 5.2,10,True]
print(dizi)

krediler=["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[1])
print(len(krediler))

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop()
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi") #indeks sırasına göre bulduğu ilk elemanı siler
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
x=10
for i in range(x):
    print("xx")
    print(i)
print("********************")
for i in range(5,10):
    print(i)
print("********************")
for i in range(0,51,10):
     print(i)
print("***************") 
# for i in range(0.1,0.5): #range fonsiyonun içi sadece integer olabilir
#     print(i)

krediler=["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler:
    print(kredi)

print("***************") 
for i in range(len(krediler)):
    print(krediler[i])

print("***************") 
#sonsuz döngü
# while True:
#     print("x")
i=0
while i<10:
    print("x")
    i+=1
print("y")

print("***************") 
while True:
    print("x")
    break

print("***************")
i=0
while i<len(krediler):
    if(krediler[i]== "Konut Kredisi"):
        break
    print(krediler[i])
    i+=1

print("***************")
i=0
while i<len(krediler):
    print(krediler[i])
    i+=1
    if(krediler[i]== "Konut Kredisi"):
        break

print("***************")
i=0
while i<len(krediler):
    i+=1
    print(krediler[i])
    if(krediler[i]== "Konut Kredisi"):
        break

#fonksiyonlar
def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")


calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Halit")
sayHello("Arif")

def calculateAndReturn(price, discount):
    return price-discount

yeniFiyat=calculateAndReturn(200,50) #fonksiyonun return değeri olduğu için yeni bir değişkene atayabildik.
print(yeniFiyat)

print("*********")
def calculatePrice(price, discount):
    print(price-discount) 

def calculatePriceAndReturn(price, discount):
    return price-discount

fonk1=calculatePrice(100,50) #None
fonk2=calculatePriceAndReturn(300,100) 
#print(f"sonuc: {fonk1+100}")#hata verir çünkü fonk1 nonetypedır
print(f"sonuc: {fonk2+100}")



