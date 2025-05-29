meus_carros = [
    {
        "marca": "Jeep",
        "modelo": "Compass",
        "ano": 2022,
        "preco_pago": 140000.00,
        "vendido": False,
        "caracteristicas": {
            "cor": "Prata",
            "transmissao": "Automática",
            "combustivel": "Flex"
        }
    },
    {
        "marca": "Honda",
        "modelo": "City",
        "ano": 2013,
        "preco_pago": 51000.00,
        "vendido": True,
        "caracteristicas": {
            "cor": "Prata",
            "transmissao": "Automática",
            "combustivel": "Flex"
        }
    },
    {
        "marca": "Fiat",
        "modelo": "UNO",
        "ano": 2000,
        "preco_pago": 10000.00,
        "vendido": True,
        "caracteristicas": {
            "cor": "Vinho",
            "transmissao": "Manual",
            "combustivel": "Gasolina"
        }
    }
]

print(meus_carros[0]["marca"])  # Acessando a marca do primeiro carro
print(meus_carros[1]["caracteristicas"]["cor"])  # Acessando a cor do segundo carro
print(meus_carros[2]["vendido"])  # Verificando se o terceiro carro foi vendido