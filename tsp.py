import pandas as pd
import numpy as np

# Carrega a matriz de distância do arquivo CSV
distance_matrix = pd.read_csv('C:\\Users\\neumann\\Documents\\projects\\get\\all_distance_matrix.csv', index_col=0)

# Converte o DataFrame para uma matriz NumPy para processamento
distances = distance_matrix.values

# Número de cidades
num_cities = len(distances)

# Função para encontrar o vizinho mais próximo não visitado
def nearest_neighbor(current_city, visited):
    nearest = None
    min_distance = float('inf')
    for i in range(num_cities):
        if not visited[i] and distances[current_city][i] < min_distance:
            nearest = i
            min_distance = distances[current_city][i]
    return nearest

# Solução usando o algoritmo do vizinho mais próximo
def tsp_nearest_neighbor(start_city=0):
    visited = [False] * num_cities
    route = [start_city]
    visited[start_city] = True
    total_distance = 0

    current_city = start_city
    while len(route) < num_cities:
        next_city = nearest_neighbor(current_city, visited)
        if next_city is not None:
            route.append(next_city)
            total_distance += distances[current_city][next_city]
            visited[next_city] = True
            current_city = next_city

    # Retorna ao ponto de partida
    total_distance += distances[current_city][start_city]
    route.append(start_city)

    return route, total_distance

# Executa o algoritmo do vizinho mais próximo
route, total_distance = tsp_nearest_neighbor()

# Exibe a rota final e a distância total
print("Rota ótima aproximada:")
print(" -> ".join(distance_matrix.index[city] for city in route))
print(f"\nDistância total percorrida: {total_distance:.2f} km")
