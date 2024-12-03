####################################
# VERİ GÖRSELLEŞTİRME: MATPLOTLİB & SEABORN
####################################

#### MATPLOTLIB

# Eğer elimizde kategorik değişken varsa : sütun grafik ile görselleştiririz. countplot bar
# Sayısal Değişken varsa : histogram, boxplot

### Kategorik Değişken Görselleştirme ###
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", None)# tüm satırları göstermeyerek ... engelledik.
pd.set_option("display.width",500)# sağ tarafa doğru daha fazla değişken
df=sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar") # kategorik değişken old. plot kullandık.
plt.show()# görselleştirmeyi aktif etmek için



### Sayısal Değişken Görselleştirme ###
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width",500)
df=sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])# sayısal değişken old. hist. kullandık
plt.show()

plt.boxplot(df["fare"]) # kutu grafiği
plt.show()




#### Matplotlib Özellikleri  #####
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width",500)

# Plot
x=np.array([1,8])
y=np.array([0,150])

plt.plot(x,y)
plt.show()

plt.plot(x,y, "X")
plt.show()


a=np.array([2,4,6,8,10])
b=np.array([1,3,77])

plt.plot(a,b,"o")
plt.show()




# marker : arraylar arası çizgi çizer.
y = np.array([13, 28, 11, 100])

plt.plot(y, marker="o")
plt.show()



# line: marker ile farkı çizgi tipini belirleyebiliyoruz
y= np.array([13,28,11,100])
plt.plot(y, linestyle="dotted")
plt.show()





# Multiple Lines
x = np.array([23, 18, 39, 44])
y = np.array([13, 27, 36, 99])
plt.plot(x)
plt.plot(y)
plt.show()



###### Labels
x= np.array([80, 85, 90, 95, 100, 105])
y= np.array([800, 805, 810, 815, 900, 905])
plt.plot(x, y)
plt.title("Bu ana başlık") # grafik başlık
plt.xlabel("X ekseni isimlendirmesi")
plt.ylabel("Y ekseni isimlendirmesi")
plt.grid() # grafiğe ızgara görünüm
plt.show()






### Subplots: Birlikte birden fazla görsel gösterilmesi

# plot 1
x= np.array([80, 85, 90, 95, 100, 105])
y= np.array([800, 805, 810, 815, 900, 905])
plt.subplot(1, 2, 1)# 1 satır 2 sütundan oluşan grafiklerin 1. si
plt.title("1. Grafik")
plt.plot(x, y)

# plot 2
x= np.array([8, 10, 12, 15, 22, 24])
y= np.array([800, 805, 810, 815, 900, 905])
plt.subplot(1, 2, 2)# 1 satır 2 sütundan oluşan grafiklerin 2. si
plt.title("2. Grafik")
plt.plot(x, y)
plt.show()



#### SEABORN ###
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset("tips")
df.head()
df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df) # kategorik değişkenlerde
plt.show()

# sayısal değişkenlerde

sns.boxplot(x=df["total_bill"])
plt.show()









