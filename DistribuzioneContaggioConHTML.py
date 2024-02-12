import folium
import pandas as pd

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')
# Crea una mappa centrata sull'Italia
m = folium.Map(location=[41.8719, 12.5674], zoom_start=5)

# Aggiungi marcatori per ogni regione
for index, row in df.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']],
                  popup=f"{row['RegionName']}: {row['TotalPositiveCases']} casi",
                  icon=folium.Icon(color='red')).add_to(m)

# Visualizza la mappa
m.save('mappa_contagi_covid.html')
