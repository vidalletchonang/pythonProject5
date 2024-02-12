import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Carica il primo dataset
df_covid = pd.read_csv('covid19_italy_region _python.csv')

# Carica il secondo dataset

df_population = pd.read_csv('Comuni _python.csv', delimiter=';', encoding='ISO-8859-1')

df_merged = pd.merge(df_covid, df_population, left_on='RegionName', right_on='Denominazione', how='inner')
threshold_population = 50000
df_merged['Categoria'] = df_merged['Popolazione2011'].apply(lambda x: 'Grande' if x > threshold_population else 'Piccola')

df_merged['Incidenza'] = df_merged['TotalPositiveCases'] / df_merged['Popolazione2011'] * 1000
plt.figure(figsize=(12, 6))
sns.boxplot(x='Categoria', y='Incidenza', data=df_merged)
plt.title('Incidenza del COVID-19 nelle Città')
plt.xlabel('Categoria')
plt.ylabel('Incidenza per 1000 abitanti')
plt.show()
