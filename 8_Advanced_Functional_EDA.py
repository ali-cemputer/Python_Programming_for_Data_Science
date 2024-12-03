#########################################################
# GELİŞMİŞ FONKSİYONEL VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#########################################################

### 1) GENEL RESİM ###
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df= sns.load_dataset("titanic")
df.head() # ilk beş değer
df.tail() # son beş değer
df.shape # satir ve sütun bilgileri
df.info() # veritipi, sütun bigileri null değerleri gibi ayrıntılı bilgileri verir
df.columns # array tipinde columns bilgileri
df.index # index bilgileri (baş, bitiş, adım)
df.describe().T # Sayısal sütunların istatiksel bilgileri (.T ise verileri transpoze(satırlar sütun, sütunlar satır olur.))
df.isnull().values.any() # boş değer var mı?
df.isnull().sum() # boş değerler toplamı


def check_df(dataframe, head=5):
    print("############################## Shape ##############################")
    print(dataframe.shape)
    print("############################## Types ##############################")
    print(dataframe.dtypes)
    print("############################## Head ##############################")
    print(dataframe.head(head))
    print("############################## Tail ##############################")
    print(dataframe.tail(head))
    print("############################## NA ##############################")
    print(dataframe.isnull().sum())

check_df(df)

df=sns.load_dataset("tips")# farklı bir df ile
check_df(df)


### 2) KATEGORİK DEĞİŞKEN ANALİZİ (ANALYSİS OF CATEGORİCAL VARİABLES) ###

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option("display.width", 500) # ekrana yazdırılan dfnin max karakter genişliği
df=sns.load_dataset("titanic")
df.head()

df["embark_town"].value_counts()
df["sex"].unique() # kategorik değişkenleri
df["class"].nunique() # kategorik değişken sayısı

# öyle birşey yapmalıyız ki veri seti içerisinden otomatik olarak kategorik değişkenleri seçsin.

cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["object", "category", "bool"]]

num_bat_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]] #numerik ama kategorik gibi davranan?

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["object", "category"]]

cat_cols= cat_cols+num_bat_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols] # categoric değişken olmayanlar


def cat_summary(DataFrame, col_name):# Fonksiyonlu hali
    print(pd.DataFrame({col_name: DataFrame[col_name].value_counts(),
                        "Ratio": 100 * DataFrame[col_name].value_counts() / len(DataFrame)}))
    print("################################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)





def cat_summary(DataFrame, col_name, plot=False):# grafikli hali
    print(pd.DataFrame({col_name: DataFrame[col_name].value_counts(),
                        "Ratio": 100 * DataFrame[col_name].value_counts() / len(DataFrame)}))
    print("################################################")

    if plot:
        sns.countplot(x=DataFrame[col_name], data=DataFrame)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("bool görselleştirilemedi")
    else:
        cat_summary(df, col, plot=True)


df["adult_male"].astype(int)


df= sns.load_dataset("titanic")
for col in df.columns:
     if df[col].dtypes=="bool":
         df[col] = df[col].astype(int)


df.info()

### 2) SAYISAL DEĞİŞKEN ANALİZİ (ANALYSIS OF NUMERICAL VARIABLES) ###

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=sns.load_dataset("titanic")
df.head()


cat_cols=[col for col in df.columns if str(df[col].dtypes) in ["object", "category", "bool"]]
num_bat_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]] #numerik ama kategorik gibi davranan?
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["object", "category"]]
cat_cols= cat_cols+num_bat_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]



df[["age","fare"]].describe().T

num_cols=[col for col in df.columns if df[col].dtypes in ["int64", "float"]]

num_cols = [col for col in df.columns if col not in cat_cols]

df.info()



### 5)Korelasyon Analizi ###

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df=pd.read_csv("titanic")
df.head()



