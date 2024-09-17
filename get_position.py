import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Leitura do CSV com pandas
df = pd.read_csv('C:\\Users\\neumann\\Documents\\projects\\get\\fixo.csv')  # Substitua 'enderecos.csv' pelo nome do seu arquivo CSV

# Inicializa o geocodificador
geolocator = Nominatim(user_agent="geoapiExercises")

# Função para obter latitude e longitude
def get_lat_long(endereco):
    try:
        location = geolocator.geocode(endereco)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except:
        return None, None

# Aplica a função de geocodificação à coluna de endereços
df['Latitude'], df['Longitude'] = zip(*df['Endereço'].apply(get_lat_long))
# Salva o novo CSV com o nome, latitude e longitude
df[['Nome', 'Latitude', 'Longitude']].to_csv('C:\\Users\\neumann\\Documents\\projects\\get\\fixo_position.csv', index=False)
