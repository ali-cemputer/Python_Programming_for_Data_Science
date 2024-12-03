# sayılar int
from mypyc.primitives.misc_ops import type_op

x=46
type(x)

# Sayılar : complex
x=2j+1
type(x)

#str
x="hello AI Era"

#boolean
True
False
type(True)
5==4

#Liste
x=["btc", "eth", "xrp"]
type(x)

# Sözlük dictionary
x={"Name": "Peter", "Age":36}
type(x)

#Tuple  (Listeden farkı normal parantez içerisine yazılmasıdır.)
x=("ali","veli","4950")
type(x)

#Set   dictionary gibi gözükür. Farkı key value ilişkisi yok.
x={"python", "ml", "ds"}
type(x)

# Not: Liste, tuple, dictionary ve set veri yapıları ayno zamanda Python Collections (Arrays ) olarak da bilinir.

########Sayılar########

a=5
b=10.5

a*3
a/7
a*b/10
a**2

#####Tipleri değiştirmek########
int(10.5)
float(a)

#Uzun string verileri için """""" kullanılır.


###################################################
#String Metodları
###################################################

dir(int)

# len fonksiyonu ifadenin karakter uzunluğunu döndürür.

#upper() lower() : küçük-büyük dönüşümleri
"miull".upper()

#replace : karakter değiştirir.

hi="Hello Aı eRA"
hi.replace("l","p")


#split : bölme
hi.split()

#capitalize : ilk harfi büyütür.


###################################################
#LİSTE (List)
###################################################

# -Değiştirilebilir
# -Sıralıdır Index işlemleri yapılabilir.
# -Kapsayıcıdır. Birden fazl veri tipini barındırabilir

notes=[1,2,3,4]#int veri tipinde
names=["a","b","c"]#str tipi
not_nam=[2,3,"a","b",True,[1,2,3]]

not_nam[0]
not_nam[5][2]


###Liste Metotları###
dir(notes)

len(notes)#uzunluk
len(not_nam)

notes.append(100)#eleman ekleme

notes.pop(0)#siler

notes.insert(0,99)#belirli indexe eleman ekleme yapar.



###################################################
#SÖZLÜK DİCTİONARY
###################################################

# Değiştirilebilirdir
# Sırasızdır. (Py 3.7den sonra sıralı hale getirilmiştir)
# Kapsayıcıdır.
#key-value yapısı vardır

dict={"ogr1":"Ahmet",
      "ogr2":"Mehmet",
      "ogr3":"ali"}

dict["ogr1"]

"ogr3" in dict


###################################################
#Demet  TUPLE
###################################################
#Değiştirilemez
#Sıralıdır
#Kapsayıcıdır

t=("john","mark",1,2)

t[0]
t[0:3]



###################################################
# Set
###################################################
#Değiştirilebilir
#Sırasız + eşsizdir
#Kapsayıcıdır

set1=set([1,3,5])
set2=set([1,2,3])













































