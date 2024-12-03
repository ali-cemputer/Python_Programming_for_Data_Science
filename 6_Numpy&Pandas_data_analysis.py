############################################
# NUMPY
############################################

#Numerical Pythonın kısaltılmışıdır. Arraylar, çok boyutlu arraylar ve matrisler üzerinde yüksek performaslı çalışmamızı sağlar.

import numpy as np
a = [1,2,3,4]
b = [2,3,4,5]
ab=[]

for i in range(0,len(a)):#Klasik yöntemler ile iki matris çarpımı
    ab.append(a[i]*b[i])

a=np.array([1,2,3,4])
b=np.array([2,3,4,5])
a*b#np ile





import numpy as np
np.array([1,2,3,4,5])
np.random.randint(0, 10, size=10)#Belirli snırlar dahilinde belirli sayıda random say üret (0 ile 10 arasında 10 tane sayı üretti)
# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a=np.random.randint(10, size=5)
a.ndim
a.shape
a.size






# Index Seçimi
b=np.random.randint(10, size=10)
b[0]
b[0:5]
a[0] = 999

m= np.random.randint(10, size=(3,5))#3 satır, 5 sütundan oluşan 0 dan 10 a kadar random sayı üret
m[2,3]# 2. satır 5. sütundaki elemanı getir.
m[:, 0]# bütün satırları seç, 0.sütunu seç
m[1: ]# 1. satır, tüm sütunları seç
m[0:2, 0:3]# 0dan 2. satıra, 0dan 3.sütuna








# Fancy Index
v=np.arange(0,30,3)# 0 dan 30 a kadar 3er 3 er artan bir dizi

catch = [1, 2, 3]

v[catch]# array içine array yazıldığında seçili indexleri getirir. 1, 2 ,3 . index







# NumPy da Koşullu işlemler
import numpy as np
x= np.array([1,2,3,4,5])

ab=[]
for i in x:# klasik döngü ile
    if i<3:
        ab.append(i)

x[x<3]# numpy ile <, >, !=, ==, >=, <= kullanılabilir.
x[x>3]
x[x!=3]
x[x==3]





# Matematiksel işlemler
import numpy as np
y=np.array([1,2,3,4,5])
y/5#bütün elemanları böler. tüm operatörler ile kullanılabilir.
np.subtract(y,1) # her elemandan 1 çıkarma işlemi
# .add : ekleme işlemi
# .mean : ort







############ PANDAS #################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])# pandas serisi oluşturmuş olduk. Series, bir liste ya da farklı tipteki veriyi pandas serisine çevirir.
type(s)# pandas.core.series.Series
s.index # başindex son index bilgileri
s.dtype # index değerlerinin veritipi
s.size # kaça elemanlı
s.ndim # kaç boyutlu
s.values # array değerleri
s.head() # ilk 5 değer
s.head(3)# ilk 3 inedexi getirir.
s.tail(4) # son 4 değer




# BU KISIM MÜKEMMELLLL ÇOK ÖNEMLİİİİİ ####################
# Veri Okuma
df=pd.read_csv("dataset/Istanbul_Weather_Data.csv")
df.head()#verilere hızlı bakış

import pandas as pd
#import seaborn as sns
#df=sns.load_dataset("titanic")# titanic datasetini import ettik
df.head() # datasete hızlı bakış
df.tail()#sondaki veriler
df.shape # datasette kaç satır sütun?
df.info() # dataset verileri bilgileri
df.columns # değişken isimleri (değişkenler sütunda yer alır)
df.index #index bilgileri
df.describe().T # verisetine analitik olarak bakmamızı sağlar
df.isnull().valueas.any() # verisetinde eksiklik var mı?
df.isnull().sum()#herbir değişkende kaç null var
df["MinTemp"].head()
df["Condition"].value_counts()

##################################################################


import seaborn as sns
df = sns.load_dataset("titanic")
# Pandas ta Seçim, atama, silme  İşlemleri
#drop : belirtilen satır veya sütunu siler.
df.index
df[0:3] #slice işlemi
df.drop(0, axis=0).head()# .drop(silinecek index, axis = satır(0) ya da  sütun(1)

delete_indexes=[1,3,5]
df.drop(delete_indexes,axis=0,inplace=True)# inplace ile kalıcı silme işlemi #1,3,5 indexlerini sildi
df["age"]# age değişkenini seçtik
df.age # değişken seçme diğer yöntemi

df.index = df.age # index yerine age atadık
df.drop("age", axis=1, inplace=True) # kalıcı olarak age sildik.

# indexi değişkene çevirmek
df["age"] = df.index # age tekrar ekledik index yerine
df.drop("age", axis=1, inplace=True)

df.reset_index().head() # resertledik






# Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df=sns.load_dataset("titanic")
df.head()

"age" in df# age değişkeni df datasetinde varmı?

df["age"].head()
df.age.head()
type(df["age"])

df[["age"]].head() # dataframe türünde almak için iki köşeli parantez kullanılır.

df[["age", "alive"]].head() # birden fazla değişken seçmek için

df["age2"] =df["age"]**2 # datasete yeni bir değişken ekleme

df.drop("age2", axis=1).head # age2 değişkeni ve sütunu sil (kalıcı olması için inplace=true yapılır)

df.loc[:, ~df.columns.str.contains("age")].head()  #içerisinde age geçen öğelerin silinmesi



#####################
# iloc & loc yapıları
#####################
# iloc: integer based selection
df.iloc[0:3]


# loc : label based selection
df.loc[0:3, "embarked"]

col_names=["age", "embarked", "alive"]
df.loc[0:3, col_names]







# Koşullu seçim (Conditional Selection)
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df=sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()# yaşı 50'den büyük olanlar
df[df["age"] > 50]["age"].count()# yaşı 50den büyük kaç tane?

df.loc[df["age"] > 50, ["age","class"]].head() # yaşı 50 den büyük olanların sınıf ve yaş bilgileri.

df.loc[(df["age"] > 40) & (df["sex"]== "male"), ["age","class"]].head()# 40 tan büyük erkeklerin yaş ve sınıf bilgileri




# Toplulaştırma ve Gruplama Fonksiyonları  ( Aggregation & Grouping ) : veri gruplarını özetler.
# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df=sns.load_dataset("titanic")
df.head()

df["age"].mean() #yaş ortalaması

df.groupby("sex")["age"].mean() # cinsiyete göre yaş ortalaması


df.groupby("sex").agg({"age": "mean"}) # cinsiyete göre yaş ort. Bu kullanım üsttekine göre daha iyi
df.groupby("sex").agg({"age": ["mean", "sum"]}) # cinsiyete göre yaş ort ve toplamı
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "embark_town" : "count"})


# Pivot Table
df.pivot_table("survived", "sex", "embarked")# cinsiyet ve biniş limanına göre hayatta kalma oranını verir
df.pivot_table("survived", "sex", ["embarked","class"])

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 30, 55, 90])# cut fonksiyonu belirtilen değişkeni belirtilen aralıklara göre böler

df.pivot_table("survived", "sex", "new_age")


####################
# Apply ve Lambda : Veri üzerinde özel işlemler yapmak için.sort
####################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500)
df=sns.load_dataset("titanic")
df.head()
#apply: bir fonk. df'in satır veya sütununa uygular
#lambda kısa, anonim fonk oluşturur. kullan at fonksiyondur
df["age2"]= df["age"]*2
df["age3"] = df["age"]*5

df[["age", "age2", "age3"]].apply(lambda x: x/10).head() #yaş değişkenlerini 10a böler

df.loc[: ,df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[: ,df.columns.str.contains("age")].apply(lambda x: (x- x.mean())/x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[: ,df.columns.str.contains("age")].apply(standart_scaler).head()

# concat ile Birleştirme İşlemleri
import numpy as np
import pandas as pd
m=np.random.randint(1, 30, (5,3))
df1=pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99 #df1'in her değişkenine 99 ekler.

pd.concat([df1, df2]) # iki df birleşti
pd.concat([df1, df2], ignore_index=True) # df2 indexleri df1in devamı olur



# merge ile birleştirme işlemleri

df1= pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                   "group": ["accouting", "engineering", "engineering", "hr"]})

df2= pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                   "start_date": [2010, 2009, 2014, 2019]})

df3 = pd.merge(df1,df2, on="employees") # iki df  employees e göre birleştirildi

# Amaç: Her çalışanın müdür bilgisine erişmek istiyoruz

df4= pd.DataFrame({"group" : ["accounting", "engineering", "hr"],
                   "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4, on="group")
