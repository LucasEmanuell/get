import pandas as pd
import numpy as np
from math import radians, sin, cos, sqrt, atan2

# Função para calcular a distância Haversine entre dois pontos
def haversine(lat1, lon1, lat2, lon2):
    # Converter graus para radianos
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    
    # Fórmula de Haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    # Raio da Terra em quilômetros (use 3956 para milhas)
    R = 6371.0
    return R * c

# Leitura do arquivo CSV
df = pd.read_csv('C:\\Users\\neumann\\Documents\\projects\\get\\all_pos.csv')

# Inicializa a matriz de distância
n = len(df)
distance_matrix = np.zeros((n, n))

# Preenche a matriz de distância usando a fórmula de Haversine
for i in range(n):
    for j in range(n):
        if i != j:  # Distância de um ponto para ele mesmo é 0
            distance_matrix[i, j] = haversine(df.iloc[i]['Latitude'], df.iloc[i]['Longitude'],
                                              df.iloc[j]['Latitude'], df.iloc[j]['Longitude'])

# Cria um DataFrame para visualização da matriz de distância
distance_df = pd.DataFrame(distance_matrix, index=df['Nome'], columns=df['Nome'])

# Exibe a matriz de distância
print(distance_df)

# Salva a matriz de distância em um novo arquivo CSV
distance_df.to_csv('C:\\Users\\neumann\\Documents\\projects\\get\\all_distance_matrix.csv', index=True)
