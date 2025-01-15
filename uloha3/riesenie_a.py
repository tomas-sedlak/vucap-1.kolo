import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Načítanie dát z Excel súboru
data_file = './uloha3/uloha3_data.xlsx'
df = pd.read_excel(data_file)

# Kontrola štruktúry dát
print("Hlavné informácie o dátach:")
print(df.info())

print("Ukážka dát:")
print(df.head())

# Výber relevantných stĺpcov
relevant_columns = ['t_cap', 't_rd', 't_hh', 'ylat']
filtered_df = df[relevant_columns]

# Výpočet korelácie
correlation_matrix = filtered_df.corr()

# Identifikácia najväčšej korelácie s kapacitou turbíny
target_corr = correlation_matrix['t_cap'].drop('t_cap').sort_values(ascending=False)

# Výsledky
print("Korelácie s kapacitou turbíny:")
print(target_corr)

# Vizualizácia korelácií
sns.pairplot(filtered_df, x_vars=['t_rd', 't_hh', 'ylat'], y_vars='t_cap', height=4, aspect=1)
plt.suptitle("Vzťah parametrov s kapacitou turbíny", y=1.02)
plt.show()

# Heatmap korelačnej matice
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Korelačná matica")
plt.show()
