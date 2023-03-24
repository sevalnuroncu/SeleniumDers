print("kodlama.io")
baslik="Taşıt Kredisi"
print(baslik)
#string => metinsel ifade
baslik="İhtiyaç Kredisi"
print(baslik)
#int, integer => tam sayı
vade=36
ekvade=6
vade2="36"

#float, decimal, double
aylikOdeme=200.50

#bool, boolean => True veya False
yukselisteMi = False

#matematiksel operatörler

# +
print(5 + 5)
print(vade +12)
print(vade + ekvade)
print(36+6)

# -
print(5-5)
print(vade-12)
print(vade-ekvade)
print(36-6)

# *
print(5*5)
print(vade*2)
print(vade*ekvade)
print(10*10)

# /
print(5/5)
print(vade/2)
print(vade/ekvade)
print(10/2)

yeniVade=vade/2
fiyat=100
indirimliFiyat=fiyat-20

print(yeniVade)
print(indirimliFiyat)

# % => mod operator
print(10%2)
print(vade%5)
print(vade%ekvade)
print(30%10)

#mantıksal operatörler
print(1==1)
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1!=1)
print(1!=2)

# or and
print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)
print(1>2 and 5>2 and 3>2)
print(2>1 or 1>2 and 3>2)

# karar yapıları
#if elif else

sayi1=15
sayi2=15
#sayi1 sayi2'den büyükse ekrana sayi1 daha büyük yazdır
#condition
#indent
if(sayi1 < sayi2):
    print("Sayi 1 Sayi 2'den küçüktür")
    print("Burası if bloğunun içidir")
elif(sayi1==sayi2):
    print("İki sayı eşittir")
#eğer if ve else if bloklarında hiçbirine girmez ise
else:
    print("Sayi 1 Sayi 2'den büyüktür")

print("*******************************")

if(sayi1 <= sayi2):
    print("Sayi 1 Sayi 2'den küçüktür")
    print("Burası if bloğunun içidir")
if(sayi1==sayi2):
    print("İki sayı eşittir")
else:
    print("Sayi 1 Sayi 2'den büyüktür")
print("Burası if bloğunun dışıdır")







