import pandas as pd
import numpy as np


url = "casos_covid.csv"
df = pd.read_csv(url)

df.loc[df['Ubicación del caso'] == 'CASA', 'Ubicación del caso'] = 'Casa'    
df.loc[df['Ubicación del caso'] == 'casa', 'Ubicación del caso'] = 'Casa'
df.loc[df['Tipo de contagio'] == 'Comunitario', 'Tipo de contagio'] = 'Comunitaria'
df.loc[df['Tipo de contagio'] == 'En Estudio', 'Tipo de contagio'] = 'En estudio'
df.loc[df['Recuperado'] == 'fallecido', 'Recuperado'] = 'Fallecido'
df.loc[df['Estado'] == 'leve', 'Estado'] = 'Leve'
df.loc[df['Estado'] == 'LEVE', 'Estado'] = 'Leve'

# punto1

casos = df.shape[0]
print(f'El total de casos es: { casos } ')

# punto2
municipios = df[df['Nombre municipio'] == 'Nombre municipio']
municipios['Nombre municipio'].value_counts()


# Punto3

municipios_afectados = pd.unique(df['Nombre municipio'])
print(f'Los municipios afectados son: { municipios_afectados } ')

# Punto4

casa = df[df['Ubicación del caso'] == 'Casa']
casa['Ubicación del caso'].value_counts()

# Punto5

recuperados = df[df['Recuperado'] == 'Recuperado']
recuperados['Recuperado'].value_counts()

# Punto6

fallecidos = df[df['Estado'] == 'Fallecido']
fallecidos['Recuperado'].value_counts()

# Punto7

df.groupby(['Tipo de contagio']).size().sort_values(ascending=False)

# Punto9

dep_afectados = pd.unique(df['Nombre departamento'])
print(f'Los departamentos afectados son: { dep_afectados } ')

# Punto10

df['Ubicación del caso'].value_counts().sort_values(ascending=False)

# Punto11

dep_casos = df[df['Estado'] == 'Leve']
dep_casos.groupby(['Nombre departamento', 'Estado']).size().head(10).sort_values(ascending=False)

# Punto12

dep_fallecidos = df[df['Estado'] == 'Fallecido']
dep_fallecidos.groupby(['Nombre departamento', 'Estado']).size().head(10).sort_values(ascending=False)

# Punto13

dep_recuperados = df[df['Recuperado'] == 'Recuperado']
dep_recuperados.groupby(['Nombre departamento', 'Recuperado']).size().head(10).sort_values(ascending=False)

# Punto14

mun_contagiados = df[df['Estado'] == 'Leve']
mun_contagiados . groupby(['Nombre municipio', 'Estado']).size().head(10).sort_values(ascending=False)

# Punto15

mun_fallecidos = df[df['Estado'] == 'Fallecido']
mun_fallecidos.groupby(['Nombre municipio', 'Estado']).size().head(10).sort_values(ascending=False)

# Punto32

df['Estado'].value_counts().sort_values(ascending=True).plot()
