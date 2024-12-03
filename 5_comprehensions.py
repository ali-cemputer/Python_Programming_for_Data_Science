### zip : aynı sayıda elemana sahip listeleri birleştiren(aynı no indexleri listeleyen.)
from pyarrow import dictionary

students=["John", "Mark", "Venessa", "Mariam"]
departments=["mathematics", "physics", "statictics", "astronomy"]
ages=[23,33, 42, 17]
ls=list(zip(students, departments, ages))
print(ls)


### lambda, map, filter, reduce

def summer(a, b):#normal def fonk.
    return a+b

#lambda
new_sum= lambda a, b : a+b# (fonk adı)= lambda (fonk.un alacağı param.) : (fonkun yapacağı iş.)
new_sum(4,5)

#map
salaries=[100,200,300,400,500]
def new_salary(x):
    return x*20/100+x

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary,salaries))#çıktı hangi yapıda olacak(map(uygulanacakfonk,üstündegezilecekdeğişken))#böylece döngü yazmamış olduk.

list(map(lambda x: x*20/100+x, salaries))#map ve lambdanın birlikte kullanımı


### LİST COMPREHENSİON ###

salaries=[1000,2000,3000,4000,5000]
def new_salary(x):#klasik yöntem
    return x*20/100+x

for salary in salaries:#klasik
    print(new_salary(salary))



[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary <3000]

[new_salary(salary*2) if salary <3000 else new_salary(salary) for salary in salaries]# list comprehension ile

### Dict Comprehension

dict= {
    "a":1,
    "b":2,
    "c":3,
    "d":4
}

dict.keys()#key değerler
dict.values()#karşılık değerler
dict.items()#key ve values

{k: v**2 for (k,v) in dict.items()}


###############################
# List & Dict Comprehensions Uygulamalar
###############################

#Bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns


for col in df.columns:
    print(col.upper())

A=[]
for col in df.columns:
    A.append(col.upper())

df.columns=A

df=sns.load_dataset("car_crashes")

df.columns=[col.upper() for col in df.columns]#comprehension ile yapılmış hali

#########################
# İsminde "INS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek istiyoruz.
#########################

["FLAG_" + col for col in df.columns if "INS" in col] # içerisinde INS olanlara FLAG_ eklendi

["FLAG_" + col if "INS" in col else "NO_FlAG_" + col for col in df.columns]# INS olanlara FLAG, olmayanlara NOFLAG eklendi


#Amaç key'i str, value'su her bir değişkenin mean,min,max.var şeklinde olan fonksiyonların olduğu sözlük oluşturmak.
# sadece sayısal değişkenler için yapmak istiyoruz

import seaborn as sns
df =sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype !="O"]#dataframe içerisinden sayısal değişkenleri seçme işlemi
soz={}# boş bir dict oluşturduk
agg_list= ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

# kısa yol.
{col: agg_list for col in num_cols}# tek satırda oluşturduk.

# agg kullanımı

new_dict = {col: agg_list for col in num_cols}
df[num_cols].agg(new_dict)







































