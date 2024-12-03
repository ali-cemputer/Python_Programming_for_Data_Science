# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayın
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
df= sns.load_dataset("titanic")
df.head() # 5 indexlik önbakış
df.shape # dataframin boyutu


# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulun
df["sex"].value_counts()


# Görev 3: Her bir sütuna ait unique değerlerin sayısını bulun
df.nunique() #unique değer: her bir satırda kaç adet benzersiz değer old. verir.
df["fare"].nunique() # nunique benzeriz değer sayısını döndürür.


# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulun
df.loc[:, "pclass"].unique() # unique benzersiz değerleri içeren dizi döndürür.


# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulun
df[["pclass", "parch"]].nunique()# dikkat! iki tane [[]] kullandı.


# Görev 6: embarked değişkeninin tipini kontrol edin. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz
df["embarked"].dtype # tip kontrolü
df["embarked"]=df["embarked"].astype("category").head() # kalıcı olması için atama yaptık.
df["embarked"].dtype


# Görev 7: embarked değeri C olanların tüm bilgilerini gösteriniz
df[df["embarked"]=="C"] # df[df{ olmasına dikkat!!


# Görev 8: embarked değeri S olmayanların tüm bilgilerini gösteriniz
df[df["embarked"] != "S"].head()


# Görev 9: Yaşı 30'dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz
df[(df["sex"]=="female") & (df["age"]<30)].head()


# Görev 10: Fare'i 500'den büyük veya yaşı 70'den büyük yolcuların bilgilerini gösteriniz
df[(df["fare"] > 500) | (df["age"] > 70)].head()


# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulun
df.isnull().sum()


# Görev 12: who değişkenini dataframe’den çıkarınız
df.drop("who", axis=0, inplace=True)# satır için 0, kalıcı olması için inplace ayarlaması yapıldı.
df.head()


# Görev 13: deck değişkenindeki boş değerleri deck değişkeninin en çok tekrar eden değeri (mode) ile doldurunuz
mod=df['deck'].mode()[0]# en çok tekrar eden değer
df["deck"].fillna(mod, inplace=True)
df.isnull().sum()


# Görev 14: age değişkenindeki boş değerleri age değişkeninin medyanı ile doldurunuz
med=df["age"].median()
df["age"].fillna(med, inplace=True)
df.isnull().sum()


# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımında sum, count, mean değerlerini bulunuz
df.groupby(["pclass", "sex"])["survived"].agg(["sum", "count" ,"mean"]) #cinsiyete ve sınıfa göre hayatta kalma oranları



# Görev 16: 30 yaşın altında olanlara 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz (apply ve lambda yapılarını kullanınız)
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)

# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız
import seaborn as sns
df=sns.load_dataset("tips")


# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
df.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 19: Günlere ve time’a göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz
df.groupby(["day","time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})


# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz
df[(df['time'] == "Lunch") & (df['sex'] == "Female")].groupby("day").agg({
    "total_bill": ["sum", "min", "max", "mean"],
    "tip": ["sum", "min", "max", "mean"]
})


# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()


# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği total_bill ve tip'in toplamını versin
df['total_bill_tip_sum'] = df['total_bill'] + df['tip']


# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız
df.sort_values(by="total_bill_tip_sum", ascending=False).head(30)# ascending= false verileri azalan sırada yapar.