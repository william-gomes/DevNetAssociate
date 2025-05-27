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

if meus_carros == []:
    print("Nenhum carro cadastrado.")
    print("Você pode cadastrar um carro agora.")
    print("Obrigado!")
elif meus_carros[0]["marca"] == "Jeep":
    print("O primeiro carro é um Jeep.")
    print (meus_carros[0]["marca"]+" "+meus_carros[0]["modelo"]+" "+str(meus_carros[0]["ano"]))
else:
    print("Há Carros cadastrados.")
    print(meus_carros[0]["marca"]+" "+meus_carros[0]["modelo"])