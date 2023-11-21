import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Se connecter à la base de données
engine = create_engine('postgresql://admin:admin@localhost:5432/test_db')

# Lire les données de la table car
query_car = 'SELECT * FROM car'
df_car = pd.read_sql_query(query_car, engine)

# Lire les données de la table consumer
query_consumer = 'SELECT * FROM consumer'
df_consumer = pd.read_sql_query(query_consumer, engine)

# Fusionner les deux DataFrames sur les colonnes Model et Year
merged_df = pd.merge(df_car, df_consumer, on=['Model', 'Year'])

print(merged_df)
# Filtrer les voitures électriques et thermiques
electric_cars = merged_df[merged_df['Engine Type'] == 'Electric']
thermal_cars = merged_df[merged_df['Engine Type'] == 'Thermal']

# Grouper par année et compter le nombre de voitures vendues
electric_cars_count = electric_cars.groupby('Year').size()
thermal_cars_count = thermal_cars.groupby('Year').size()
 
# Plot 1
plt.figure(figsize=(10, 6))
plt.plot(electric_cars_count.index, electric_cars_count.values, label='Electric Cars')
plt.plot(thermal_cars_count.index, thermal_cars_count.values, label='Thermal Cars')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
plt.title('Electric vs Thermal Cars Sold Per Year')
plt.legend()
plt.show()

# Plot 2
plt.figure(figsize=(10, 6))
plt.bar(electric_cars_count.index, electric_cars_count.values, label='Electric Cars')
plt.bar(thermal_cars_count.index, thermal_cars_count.values, bottom=electric_cars_count.values, label='Thermal Cars')
plt.xlabel('Year')
plt.ylabel('Number of Cars Sold')
plt.title('Electric vs Thermal Cars Sold Per Year')
plt.legend()
plt.show()
