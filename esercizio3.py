import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')
# Assicurati che la colonna 'Date' sia nel formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Estrai l'anno e il trimestre dalla colonna 'Date'
df['Year'] = df['Date'].dt.year
df['Quarter'] = df['Date'].dt.quarter

# Raggruppa per trimestre e regione e calcola la somma dei nuovi casi positivi
grouped_data = df.groupby(['Year', 'Quarter', 'RegionName'])['NewPositiveCases'].sum().reset_index()

# Normalizza la colonna 'NewPositiveCases' utilizzando MinMaxScaler
scaler = MinMaxScaler()
grouped_data['NewPositiveCases_Normalized'] = scaler.fit_transform(grouped_data[['NewPositiveCases']])

# Visualizza i dati normalizzati raggruppati per trimestre e regione con un grafico a barre
plt.figure(figsize=(15, 8))
sns.barplot(x='RegionName', y='NewPositiveCases_Normalized', hue='Year', data=grouped_data)
plt.title('Somma dei Nuovi Casi Positivi (Normalizzati) per Trimestre e Regione')
plt.xlabel('Regione')
plt.ylabel('Nuovi Casi Positivi (Normalizzati)')
plt.xticks(rotation=45)
plt.legend(title='Anno', bbox_to_anchor=(1, 1))
plt.show()


"""import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')
# Assicurati che la colonna 'Date' sia nel formato datetime
df['Date'] = pd.to_datetime(df['Date'])

# Estrai l'anno e il trimestre dalla colonna 'Date'
df['Year'] = df['Date'].dt.year
df['Quarter'] = df['Date'].dt.quarter

# Raggruppa per trimestre e regione e calcola la somma dei nuovi casi positivi
grouped_data = df.groupby(['Year', 'Quarter', 'RegionName'])['NewPositiveCases'].sum().reset_index()

# Visualizza i dati raggruppati per trimestre e regione
plt.figure(figsize=(15, 8))
sns.scatterplot(x='Year', y='Quarter', hue='RegionName', size='NewPositiveCases', data=grouped_data)
plt.title('Somma dei Nuovi Casi Positivi per Trimestre e Regione')
plt.xlabel('Anno')
plt.ylabel('Trimestre')
plt.legend(title='Regione', bbox_to_anchor=(1, 1))
plt.show()"""
