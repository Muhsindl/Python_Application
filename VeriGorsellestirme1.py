import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

veriTablo = pd.read_excel("tablo_ambulans.xlsx")
veriTablo = veriTablo.set_index("Yıl")

# Çubuk grafiklerini çizme
plt.figure(figsize=(6,8))
sns.barplot(x="Yıl", y="Medikal", data=veriTablo, alpha=0.3,label="Medikal")
sns.barplot(x="Yıl", y="Trafik Kazası", data=veriTablo, alpha=0.3,label="Trafik Kazası")
sns.barplot(x="Yıl", y="Diğer Kazalar", data=veriTablo, alpha=0.3,label="Diğer Kazalar")
sns.barplot(x="Yıl", y="Yaralanma", data=veriTablo, alpha=0.3,label="Yaralanma")
sns.barplot(x="Yıl", y="İntihara Teşebbüs", data=veriTablo, alpha=0.3,label="İntihara Teşebbüs")
sns.barplot(x="Yıl", y="Yangın", data=veriTablo, alpha=0.3,label="Yangın")
sns.barplot(x="Yıl", y="Sağlık Tedbirleri", data=veriTablo, alpha=0.3,label="Sağlık Tedbirleri")
sns.barplot(x="Yıl", y="Şehirlerarası Nakil", data=veriTablo, alpha=0.3,label="Şehirlerarası Nakil")
sns.barplot(x="Yıl", y="Diğerleri", data=veriTablo, alpha=0.3,label="Diğerleri")

plt.legend(loc='upper right',frameon = True)
plt.xlabel("Yıl",color="darkblue")
plt.ylabel("Durumlar",color="darkblue")
plt.title("Ambulans Çağrılma Durumu",color="magenta")
plt.show()
