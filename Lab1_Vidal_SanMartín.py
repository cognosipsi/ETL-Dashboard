#Valentina San Martin
#Andres Vidal
import numpy as np
import pandas as pd

# Carga el archivo CSV en un DataFrame
df = pd.read_csv('netflix_titles.csv', encoding='latin1')
df = df[~df.apply(lambda row: any(row.astype(str).str.contains('\n')), axis=1)]

# Se obtiene el número de columnas en el DataFrame
num_columnas = len(df.columns)

# Se obtienen los nombres de las columnas
nombres_columnas = df.columns

# Itera sobre cada columna para contar los elementos de valor distinto a NaN (columnas sin valor)
for i in range(num_columnas):
    # Nombre de la columna actual
    nombre_columna = nombres_columnas[i]
    # Cuenta los elementos de valor distinto a NaN en la columna actual
    num_no_nan = df.iloc[:, i].count()
    print("Número de elementos diferentes de NaN en la columna", nombre_columna, ":",num_no_nan)

#Elimina las columnas con NaN
df = df.dropna(axis=1, how='all')

# Se obtiene el número de columnas en el DataFrame después de eliminar las columnas con NaN
num_columnas_despues = len(df.columns)

print("Número de columnas antes de eliminar las columnas con NaN:", num_columnas)
print("Número de columnas después de eliminar las columnas con NaN:", num_columnas_despues)

df['director'].fillna("not specified", inplace=True)
df['cast'].fillna("not specified", inplace=True)
df['country'].fillna("not specified", inplace=True)
df['date_added'].fillna("not specified", inplace=True)
df['rating'].fillna("not specified", inplace=True)
df['duration'].fillna("not specified", inplace=True)

# Elimina el carácter 's' al principio de los IDs
df['show_id'] = df['show_id'].str[1:]

df['show_id'] = range(1, len(df) + 1)

df = df.dropna(subset=df.columns, how='any')

#Se genera el archivo modificado
df.to_csv('netflix_titles_modified.csv', index=False)