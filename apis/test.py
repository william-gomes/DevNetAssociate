import requests

# Coordenadas para São Paulo
latitude = -19.976304846380046
longitude = -43.99859950003238

url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
)

# Fazendo a requisição GET
resposta = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados["current"]["temperature_2m"]
    vento = dados["current"]["wind_speed_10m"]
    print(f"Temperatura atual: {temperatura}°C")
    print(f"Velocidade do vento: {vento} km/h")
else:
    print("Erro na requisição:", resposta.status_code)
