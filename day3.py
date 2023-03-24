#sınıflar => classlar
#modules
#paket yönetimi
#self => this => fonksiyon içinde class içindeki diğer alanlara erişmek için kullanılır

class Human:
    name="Halit"
    #built-in = hazır fonksiyonlar __init__
    #constructor
    #initialize
    def __init__(self,name):
        self.name=name
        print("bir human instance i üretildi")
    def __str__(self):
        return f"STR fonksiyonundan dönen deger: {self.name}"
    def talk(self,sentence):
        print(f"Human: {sentence}")
        name="Ercan"
        print(f"{name}:{sentence}")     #fonksiyon içindeki name
        print(f"{self.name}:{sentence}")# class altındaki name
        self.walk()
    def walk(humanObj):
        print("Human is walking..")

#instance => örnek
human1=Human("Enes")   
#human1.name="Enes"
human1.talk("Merhaba") 
human1.walk()
print(human1)

human2=Human("Enes")
#human2.name="Cem"
human2.talk("Selam")
human2.walk()
print(human2)

