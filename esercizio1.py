import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')

# 1. Andamento temporale
"""df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df['NewPositiveCases'], label='Nuovi casi positivi')
plt.plot(df['Recovered'], label='Guariti')
plt.plot(df['Deaths'], label='Decessi')
plt.title('Andamento temporale')
plt.xlabel('Data')
plt.ylabel('Numero di casi')
plt.legend()
plt.show()"""

# Normalizzazione delle colonne 'NewPositiveCases', 'Recovered' e 'Deaths'
normalized_new_cases = (df['NewPositiveCases'] - df['NewPositiveCases'].mean()) / df['NewPositiveCases'].std()
normalized_recovered = (df['Recovered'] - df['Recovered'].mean()) / df['Recovered'].std()
normalized_deaths = (df['Deaths'] - df['Deaths'].mean()) / df['Deaths'].std()

# Plot normalizzato
plt.figure(figsize=(12, 6))
plt.plot(normalized_new_cases, label='Nuovi casi positivi (Normalizzato)')
plt.plot(normalized_recovered, label='Guariti (Normalizzato)')
plt.plot(normalized_deaths, label='Decessi (Normalizzato)')
plt.title('Andamento temporale (Normalizzato)')
plt.xlabel('Data')
plt.ylabel('Numero di casi (Normalizzato)')
plt.legend()
plt.show()


# 2. Distribuzione geografica
plt.figure(figsize=(10, 8))
sns.scatterplot(x='Longitude', y='Latitude', hue='TotalPositiveCases', size='TotalPositiveCases', data=df)
plt.title('Distribuzione geografica dei casi')
plt.xlabel('Longitudine')
plt.ylabel('Latitudine')
plt.show()

# 3. Analisi delle regioni
regioni_analysis = df.groupby('RegionName')[['TotalPositiveCases', 'Recovered', 'Deaths']].sum()
regioni_analysis['LetalityRate'] = regioni_analysis['Deaths'] / regioni_analysis['TotalPositiveCases'] * 100

# 4. Capacità ospedaliera
plt.figure(figsize=(12, 6))
sns.barplot(x='RegionName', y='TotalHospitalizedPatients', data=df)
plt.title('Capacità ospedaliera per regione')
plt.xlabel('Regione')
plt.ylabel('Pazienti ospedalizzati')
plt.xticks(rotation=45)
plt.show()

# 5. Analisi delle correlazioni
# Escludi colonne non numeriche dalla matrice di correlazione
correlation_matrix = df.select_dtypes(include=[np.number]).corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di correlazione tra variabili')
plt.show()

# 6. Predizione futura (esempio: media mobile)
df['NewPositiveCases_MovingAvg'] = df['NewPositiveCases'].rolling(window=7).mean()

# Visualizza l'andamento temporale e la media mobile
plt.figure(figsize=(12, 6))
plt.plot(df['NewPositiveCases'], label='Nuovi casi positivi', linestyle='-', marker='o')
plt.plot(df['NewPositiveCases_MovingAvg'], label='Media mobile (window=7)', linestyle='-', marker='o')
plt.title('Andamento temporale e Media mobile dei nuovi casi positivi')
plt.xlabel('Data')
plt.ylabel('Numero di casi')
plt.legend()
plt.show()