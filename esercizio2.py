import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Carica il dataset
df = pd.read_csv(r'C:\Users\vidal\PycharmProjects\pythonProject5\covid19_italy_region _python.csv')
# Rimuovi le righe con etichette di indice duplicate
df = df[~df.index.duplicated(keep='first')]

# Resetta gli indici
df.reset_index(drop=True, inplace=True)

# 7. Predizione futura (esempio: media mobile)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Aggiungi la colonna della media mobile
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


