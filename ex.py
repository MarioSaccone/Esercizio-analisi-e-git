import numpy as np
import pandas as pd
from sklearn import datasets

# Branch 1 – Esplorazione iniziale
# Caricamento del dataset Iris
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = data.target
species_names = {i: name for i, name in enumerate(data.target_names)}
df['species'] = df['species'].map(species_names)

# Verifica delle informazioni di base
print("Informazioni del dataset:")
print(df.info())
print("\nStatistiche descrittive:")
print(df.describe())
print("\nNumero di specie uniche:")
print(df['species'].value_counts())
