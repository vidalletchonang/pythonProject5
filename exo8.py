import pandas as pd
import matplotlib.pyplot as plt

# Leggi il dataset
df = pd.read_csv('covid19_italy_region _python.csv')

# Seleziona solo le colonne necessarie
df_hospitalized = df[['RegionName', 'HospitalizedPatients']]

# Raggruppa per regione e calcola la somma dei pazienti ospedalizzati
df_hospitalized_sum = df_hospitalized.groupby('RegionName')['HospitalizedPatients'].sum().reset_index()

# Ordina il dataframe in base al numero di pazienti ospedalizzati in ordine decrescente
df_hospitalized_sum = df_hospitalized_sum.sort_values(by='HospitalizedPatients', ascending=False)

# Crea un grafico a barre per la distribuzione dei pazienti ospedalizzati per regione
plt.figure(figsize=(12, 6))
plt.bar(df_hospitalized_sum['RegionName'], df_hospitalized_sum['HospitalizedPatients'], color='skyblue')

plt.title('Numero di Pazienti Ospedalizzati per Regione')
plt.xlabel('Regione')
plt.ylabel('Regione le piu Colpite')
plt.xticks(rotation=45, ha='right')

# Mostra il grafico
plt.tight_layout()
plt.show()
