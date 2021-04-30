import pandas as pd

# pd.read_csv() est une fonction de pandas qui permet de lire directement un fichier csv en indiquant son path
movies_df = pd.read_csv('IMDB-Movie-Data.csv', index_col="Title",sep=",")
# La fonction head() : Head prend les premieres lignes du fichier csv
print(movies_df.head())
# La fonction info() : Nous donne des information concernant le data frame
# Le nombre de lignes, de colonnes, le type de données .. ect
print(movies_df.info())

# shape represente le nombre de lignes et de colonnes contenues dans le data frame as dataset
print("dataset=", movies_df.shape)

# Retourne les label des colonnes du data frame as Columns
print("Columns=", movies_df.columns)


print("\n--- origine ---")
print(movies_df.info())
print("\n--- Drop 0 ---")
# On crée un nouveau data frame temporaire
# Par defaut dropna() supprime les lignes contenant des vides
# ce qui explique la diminution du nombre de lignes (1000 -> 838) dans temp_df
temp_df = movies_df.dropna()
print(temp_df.info())
print("\n--- Drop 1 ---")
# dropna("columns") elimine les colonnes contenant des valeurs vides
# Ce qui explique le passage de 12 a 10 colonnes dans le data frame temp_df
temp_df = movies_df.dropna("columns")
print(temp_df.info())

print("\n--- origine ---")
print(movies_df.info())

# Crée un "Series" les titres ainsi que leurs Revenue uniquement (une sorte de Select)
revenue = movies_df['Revenue (Millions)']
# Mean calcule la moyenne arithmetique (82.95 dans notre cas)
revenue_mean = revenue.mean()
# fillna insert une valeur dans les lignes contenant des vides
# Dans notre cas la valeur inserée sera la moyenne calculée plus haut
temp_df = movies_df.fillna(value={'Revenue (Millions)': revenue_mean})
print("\n--- --  ---")

df_temp = temp_df.isnull().sum()
# isnull detecte les valuers nulles et renvoi un tableau contenant
# des booléen vrai si la valeur est vide
# dans notre cas les sommes calculées sont 0
print(temp_df.isnull().sum())
print("\n--- Fill  ---")
print(temp_df.info())

# Génere les statistques descriptives de chaque colonne dans notre data frame
print("\n------- Descrition ---------")
print(temp_df.describe())

# Génere les statistiques descriptives calculées a partir de la colonne 'Genre'
print("\n", movies_df['Genre'].describe())

# Retourne les 10 premiers count calculés a partir de la colonne 'Genre' des
print("\n", movies_df['Genre'].value_counts().head(10))
a = movies_df['Genre'].value_counts().head(10)
