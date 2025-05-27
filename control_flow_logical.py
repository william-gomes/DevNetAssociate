# meus_carros = [
#     {
#         "marca": "Jeep",
#         "modelo": "Compass",
#         "ano": 2022,
#         "preco_pago": 140000.00,
#         "vendido": False,
#         "caracteristicas": {
#             "cor": "Prata",
#             "transmissao": "Automática",
#             "combustivel": "Flex"
#         }
#     },
#     {
#         "marca": "Honda",
#         "modelo": "City",
#         "ano": 2013,
#         "preco_pago": 51000.00,
#         "vendido": True,
#         "caracteristicas": {
#             "cor": "Prata",
#             "transmissao": "Automática",
#             "combustivel": "Flex"
#         }
#     },
#     {
#         "marca": "Fiat",
#         "modelo": "UNO",
#         "ano": 2000,
#         "preco_pago": 10000.00,
#         "vendido": True,
#         "caracteristicas": {
#             "cor": "Vinho",
#             "transmissao": "Manual",
#             "combustivel": "Gasolina"
#         }
#     }
# ]
code = 210
match code:
    case 404:
        print("Not Found")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 301:
        print("Moved Permanently")
    case 500:
        print("Internal Server Error")
    case 200:
        print("Success")
    case _: # Default case for any other status code
        print("Unknown Status Code")

