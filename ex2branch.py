# Branch 2 – Analisi approfondita
# Calcolo della correlazione tra le variabili
correlation_matrix = df.corr(numeric_only=True)
print("\nMatrice di correlazione:")
print(correlation_matrix)

# Raggruppamento per specie e calcolo statistiche
grouped = df.groupby('species').agg(['mean', 'max'])
print("\nStatistiche per specie (media e massimo):")
print(grouped)

# Confronto dei valori medi e massimi delle diverse caratteristiche
print("\nConfronto delle caratteristiche tra le specie:")
for feature in data.feature_names:
    print(f"Caratteristica: {feature}")
    for stat in ['mean', 'max']:
        print(f"  {stat.capitalize()} per specie:")
        print(df.groupby('species')[feature].agg(stat))
    print()
