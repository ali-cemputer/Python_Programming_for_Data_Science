################
### Görev 1: ### Verilen değerlerin veri yapılarını incele.
################

x=8
type(x)
y=3.2
type(y)
z=8j+18
type(z)
a="Hello World"
b=True

################
### Görev 2: ### Verilen ifadenin tüm harflerini büyük çevir. Virgül ve nokta yerine space koy. Kelime kelime ayır.
################

text = "The goal is to turn data into information, and information into insight"
text = text.upper()
text = text.replace(",", " ").replace(".", " ")
words = text.split()
print(words)

################
### Görev 3: ### Verilen listeyi aşa. adımları izle.
################

lst = ["D", "A", "T", "A", "I", "S", "T", "H", "E", "B", "E", "S", "T"]

# Listenin eleman sayısına bak.
len(lst)

#Sıfırıncı ve onuncu index
lst[0]
lst[10]

# ["D", "A", "T", "A"] listesi oluşturunuz.
lst[0:4]

# Sekizinci indexi sil.
lst.pop(7)

#Yeni bir eleman ekleyiniz.
lst.append("new")

# Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(7,"N")

################
### Görev 4: ### Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
################
dict={"Christian" : ["America", 18],
      "Daisy" : ["England", 12],
      "Antonio" : ["Spain", 22],
      "Dante" : ["Italy", 25]
      }
# Key değerlerine eriş.
dict.keys()

# Value'lara eriş
dict.values()

# Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict["Daisy"][1]=13

#Key değeriAhmet value değeri[Turkey,24] olan yeni bir değer ekleyiniz.
dict["Ahmet"] = ["Turkey", 24]

#Antonio'yu dictionary'den siliniz.
dict.pop("Antonio")
dict


################
### Görev 5: ### Argümanolarakbir liste alan, listenin içerisindeki tek ve çift sayıları
# ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.
################

l = [2,13,18,93,22]
C=[]
T=[]
def func(list):
    for x in list:
        if(x%2==0):
            C.append(x)
        else:
            T.append(x)
    return C,T

even_list, odd_list= func(l)


################
### Görev 6: ### Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin
# isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken
# son üç öğrenci de tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini
# fakülte özelinde yazdırınız.
################
ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler):
    if index < 3:
        print(f"Mühendislik Fakültesi {index+1}. öğrenci: {ogrenci}")
    else:
        print(f"Tıp Fakültesi {index-2}. öğrenci: {ogrenci}")


################
### Görev 7: ### Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi
# ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
################
ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]


for kod, krd, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {krd} olan {kod} kodlu dersin kontenjanı {kont} kişidir.")



################
### Görev 8: ### Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor
# ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
################
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kontrol_et(kume1, kume2):
    if kume1.issuperset(kume2):  # Kume1, Kume2'yi kapsıyor mu?
        print(kume1.intersection(kume2))  # Ortak elemanları yazdır
    else:
        print(kume2.difference(kume1))  # Kume2'nin farkını yazdır


