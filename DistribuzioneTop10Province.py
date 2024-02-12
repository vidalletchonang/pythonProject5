import pandas as pd
import matplotlib.pyplot as plt

# Leggi il dataset
df = pd.read_csv('covid19_italy_province _python.csv')

# Filtra solo le colonne necessarie
df_province = df[['ProvinceName', 'TotalPositiveCases']]

# Raggruppa per provincia e calcola il totale dei casi positivi
df_province_sum = df_province.groupby('ProvinceName')['TotalPositiveCases'].sum().reset_index()

# Ordina il dataframe per il totale dei casi positivi in ordine decrescente
df_province_sum = df_province_sum.sort_values(by='TotalPositiveCases', ascending=False)

# Seleziona solo le prime 10 province per evitare sovrapposizioni
top_province = df_province_sum.head(10)

# Crea un grafico a barre orizzontali
plt.figure(figsize=(12, 6))
plt.barh(top_province['ProvinceName'], top_province['TotalPositiveCases'], color='skyblue')

# Regola l'etichetta dell'asse y per una migliore leggibilità
plt.xlabel('Numero Totale di Casi Positivi')
plt.ylabel('Provincia')
plt.title('Distribuzione dei Casi Positivi per Provincia (Top 10)')
plt.tight_layout()
plt.show()




