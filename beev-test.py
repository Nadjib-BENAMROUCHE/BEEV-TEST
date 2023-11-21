import pandas as pd
from sqlalchemy import create_engine

try:
    # Lire les fichiers CSV
    df_car = pd.read_csv('csv_data/car_data.csv')

    # Spécifier les noms de colonnes pour le DataFrame df_consumer, car il y a un problème avec les noms de colonnes
    column_names = ['Country', 'Make', 'Model', 'Year', 'Review Score', 'Sales Volume']

    # Lire le fichier CSV en utilisant les noms de colonnes spécifiés
    df_consumer = pd.read_csv('csv_data/consumer_data.csv', names=column_names, skiprows=1)
    #print(df_consumer)

    # Gestion des erreurs lors de la lecture des fichiers CSV
except FileNotFoundError as e:
    print(f"Erreur : {e}")

# Prétraitement de données (Mapping)
model_make_mapping = df_car.set_index('Model')['Make'].to_dict()
df_consumer['Make'] = df_consumer['Model'].map(model_make_mapping)

# Sauvegarder le DataFrame en tant que fichier CSV pour la vérification
#df_consumer.to_csv('csv_data/new_consumer_data.csv', index=False)

# Se connecter à la base de données initiée par docker-compose
try:
    engine = create_engine('postgresql://admin:admin@localhost:5432/test_db')

    # Insérer les données dans la base de données
    df_car.to_sql('car', engine, index=False, if_exists='replace')
    df_consumer.to_sql('consumer', engine, index=False, if_exists='replace')

except Exception as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
