import pandas as pd
import numpy as np

# Carrega a matriz de distância do arquivo CSV
distance_matrix = pd.read_csv('C:\\Users\\neumann\\Documents\\projects\\get\\all_distance_matrix.csv', index_col=0)

# Converte o DataFrame para uma matriz NumPy para processamento
distances = distance_matrix.values

# Número de clientes (considerando o índice 0 como depósito)
num_clients = len(distances)

# Inicializa a rota de cada cliente para o depósito
routes = [[0, i, 0] for i in range(1, num_clients)]

# Função para calcular a economia de combinar duas rotas
def saving(i, j):
    return distances[0][i] + distances[0][j] - distances[i][j]

# Calcula a lista de economias para todas as combinações de clientes
savings_list = [(i, j, saving(i, j)) for i in range(1, num_clients) for j in range(i + 1, num_clients)]
# Ordena pela maior economia
savings_list.sort(key=lambda x: x[2], reverse=True)

# União de rotas
for i, j, s in savings_list:
    route_i = next((r for r in routes if r[1] == i and r[-2] == 0), None)
    route_j = next((r for r in routes if r[1] == j and r[-2] == 0), None)
    
    if route_i and route_j and route_i != route_j:
        # Concatena as rotas
        new_route = route_i[:-1] + route_j[1:]
        # Remove as rotas antigas
        routes.remove(route_i)
        routes.remove(route_j)
        # Adiciona a nova rota
        routes.append(new_route)

# Calcula a distância total percorrida
total_distance = 0
for route in routes:
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]

# Exibe as rotas finais e a distância total
print("Rotas otimizadas:")
for route in routes:
    print(" -> ".join(map(str, route)))

print(f"\nDistância total percorrida: {total_distance:.2f} km")
