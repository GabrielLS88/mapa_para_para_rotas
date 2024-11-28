import folium
import openrouteservice

# Configurar a chave de API
API_KEY = '5b3ce3597851110001cf6248868901d91f6c4c89b20a7a8027bba612'

# Coordenadas de exemplo (origem e destino)
origem = (-23.55052, -46.633308)  # São Paulo
destino = (-22.906847, -43.172896)  # Rio de Janeiro

# Criar cliente do OpenRouteService
client = openrouteservice.Client(key=API_KEY)

# Solicitar rota
rota = client.directions(
    coordinates=[origem[::-1], destino[::-1]],
    profile='driving-car',  # Pode ser 'walking', 'cycling', etc.
    format='geojson'
)

# Extraindo informações da rota
distancia = rota['routes'][0]['summary']['distance'] / 1000  # Em km
duracao = rota['routes'][0]['summary']['duration'] / 60  # Em minutos
coordenadas_rota = rota['routes'][0]['geometry']

print(f"Distância: {distancia:.2f} km")
print(f"Duração: {duracao:.2f} minutos")

# Criar mapa centralizado na origem
mapa = folium.Map(location=origem, zoom_start=6)

# Adicionar a rota ao mapa
folium.GeoJson(coordenadas_rota).add_to(mapa)

# Adicionar marcadores
folium.Marker(origem, tooltip="Origem (São Paulo)").add_to(mapa)
folium.Marker(destino, tooltip="Destino (Rio de Janeiro)").add_to(mapa)

# Salvar mapa como arquivo HTML
mapa.save("mapa_rota.html")

print("Mapa gerado e salvo como 'mapa_rota.html'.")
