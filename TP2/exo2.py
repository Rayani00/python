from os import sep
from numpy import NaN
import pandas as pd
import numpy as np
import csv


# PART 1

df_jobs = pd.read_csv("jobs.csv", index_col="Job #", sep=";")

# On crée une liste contenant le nom des colonnes
with open('jobs.csv', 'r') as f:
    firstLine = f.readline()


# on crée une Serie contenant les colonnes ainsi que le nombre de lignes
# nulles contenues dans la colonne
a = df_jobs.isna().sum()
columns = firstLine.split(";")
columns.remove("Job #")
print(columns)
nbColProb = 0
for col in columns:
    # A partir de la Colonne on crée une liste
    listCol = df_jobs[col].tolist()
    # On recupére le nombre de lignes
    nbElt = len(listCol)
    # On calcule le nombre de valeurs manquantes dans la colonne
    nbEltNull = sum(x is NaN for x in listCol)
    # Si celle ci depasse 80% on dit qu'elle est problematique
    if((nbEltNull*100/nbElt) >= 80):
        # print(f"{col} contient {nbElt} lignes et {nbEltNull} lignes nulles.")
        print(f"La colonne {col} est problematique.")
        nbColProb += 1


print(f"Le nombre de colonnes problematiques est {nbColProb}")

# Delete the outlier using quantiles in pandas

for col in columns:
    if((df_jobs.dtypes[col] == np.float64) or (df_jobs.dtypes[col] == np.int64)):
        # Créer un data frame
        df = pd.DataFrame(df_jobs[columns.index(col)])
        # Fixer les limites
        lowerBound = 0.15
        upperBound = 0.85
        # Filter
        res = df.quantile([lowerBound, upperBound])
        std = df[col].std()
        # On calcule la mediane
        mid = res.median()
        # les outliers
        outliers = (df[col] - mid).abs() > std
        # On insére la mediane dans les valeurs outliers
        df[outliers] = np.nan
        df[col].fillna(mid, inplace=True)

# Check formating data

for col in columns:
    # If date strings are in good format they'll stay the same else their format will change
    pd.to_datetime(df_jobs[columns.index(col)], format='%y/%m/%d %H:%M:%S')


# Dependent columns

# Splitting dataFrame into independent feature matrix
# Get independent feature matrix
x = df_jobs.iloc[:, :-1].values
# Get dependent feature matrix
y = df_jobs.iloc[:, -1].values


# PART 2


colList = []
for col_name in df_jobs.columns:
    colList.append(col_name)


# Replace missing values
for col in colList:
    if((df_jobs.dtypes[col] == np.float64) or (df_jobs.dtypes[col] == np.int64)):
        # Fill with the average
        df_jobs[col].fillna((df_jobs[col].mean()), inplace=True)
        # Fill with the max
        """ df_jobs[col].fillna((df_jobs[col].max()), inplace=True) """
        # Fill with the min
        """ df_jobs[col].fillna((df_jobs[col].min()), inplace=True) """

    else:
        # Get the max counted value
        # Sort the elements by their count and select the first(the max counted)
        serieMaxCountedVal = df_jobs[col].value_counts().head(1)
        # Get the index value
        maxCountValue = serieMaxCountedVal.first_valid_index()
        # Put the maxCountValue in the NaN
        df_jobs[col].fillna(maxCountValue, inplace=True)


# Replace outliers with nulls in padas
for col in columns:
    if((df_jobs.dtypes[col] == np.float64) or (df_jobs.dtypes[col] == np.int64)):
        # Créer un data frame
        df = pd.DataFrame(df_jobs[columns.index(col)])
        # Fixer les limites
        lowerBound = 0.15
        upperBound = 0.85
        # Filter
        res = df.quantile([lowerBound, upperBound])
        std = df[col].std()
        # On calcule la mediane
        mid = res.median()
        # les outliers
        outliers = (df[col] - mid).abs() > std
        # On insére la mediane dans les valeurs outliers
        df[outliers] = np.nan
        df[col].fillna(None, inplace=True)
