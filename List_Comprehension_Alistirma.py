################
### Görev 1: ### ListComprehension yapısı kullanarak car_crashes verisindeki numeric
# değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
################
import seaborn as sns

# Veriyi yükleyelim
df = sns.load_dataset("car_crashes")

# List Comprehension ile istenilen işlemi yapalım
new_columns = ["NUM_" + col.upper() if df[col].dtype != 'O' else col.upper() for col in df.columns]

# Sonuç
#print(new_columns)


################
### Görev 2: ### ListComprehension yapısı kullanarak car_crashes verisinde isminde"no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.
################
import seaborn as sns
df = sns.load_dataset("car_crashes")

new2_columns=[col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns]
#print(new2_columns)


################
### Görev 3: ###  ListComprehension yapısı kullanarak aşağıda verilen değişken isimlerinden
# FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz
################


import seaborn as sns
df = sns.load_dataset("car_crashes")

og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]

new_df = df[new_cols]

# Sonucu gösterelim
print(new_df)














