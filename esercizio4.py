import pandas as pd

# Sostituire 'percorso_del_tuo_file.txt' con il percorso effettivo del file di testo
# file_path = 'percorso_del_tuo_file.txt'
file_path = r'C:\Users\vidal\PycharmProjects\pythonProject5\Ripartizione-geografica _python.txt'


# Caricare il DataFrame dal file di testo specificando l'encoding
df_regioni = pd.read_csv(file_path, delimiter='\t', encoding='ISO-8859-1')

# Visualizzare il DataFrame
print("Informazioni sul dataset delle regioni:")
print(df_regioni.info())

# Stampare le prime righe del DataFrame
print("\nPrime 5 righe del dataset delle regioni:")
print(df_regioni.head())



