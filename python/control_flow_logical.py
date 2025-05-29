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
# code = 210
# match code:
#     case 404:
#         print("Not Found")
#     case 401:
#         print("Unauthorized")
#     case 403:
#         print("Forbidden")
#     case 301:
#         print("Moved Permanently")
#     case 500:
#         print("Internal Server Error")
#     case 200:
#         print("Success")
#     case _: # Default case for any other status code
#         print("Unknown Status Code")

meus_carros[0] = None

# # Exemplo de uso de try/except para tratamento de erros
# for carro in meus_carros:    
#     try:
#         print(carro["marca"], carro["modelo"], carro["ano"])
#         if carro["marca"] == "Jeep": 
#             print("Jeep encontrado! Boa compra!")
#             break #Se encontrar um Jeep, encerra o loop, nao importa o resto
#         else:
#             continue #Continua o loop para o próximo carro, mas não executa o restante do código abaixo
#     except TypeError as e:
#         print("Encontrei um erro")
#         print(e)
#     else:
#         print("Nenhum erro encontrado.")
#     print("Teste para mostrar que break e continue funcionam") #Nao imprime porque o loop é interrompido pelo break e o continue não executa o restante do for

# print("Fim do loop") #Executa normalmente porque está fora do loop

# Exemplo de uso de try/except para tratamento de erros
for carro in meus_carros:    
    try: #Tenta executar o código dentro do bloco try
        print(carro["marca"], carro["modelo"], carro["ano"])
        if carro["marca"] == "Jeep": 
            print("Jeep encontrado! Boa compra!")
        else:
            print("Carro não é um Jeep, continuando...")
    except TypeError as e: # Captura o erro de tipo, caso o carro seja None
        print("Encontrei um erro")
        print(e)
    else: # Se não houver erro, executa este bloco
        print("Nenhum erro encontrado.")
    finally:  # Este bloco é sempre executado, independentemente de erro ou não
        print("O código continua aqui, independentemente")


# if any(carro["vendido"] for carro in meus_carros):
#     print("Alguns carros já foram vendidos.")
# else:
#     print("Nenhum carro foi vendido ainda.")
