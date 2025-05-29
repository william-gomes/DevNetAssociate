# import os
import json

# # Caminho absoluto do arquivo atual
# base_path = os.path.dirname(__file__)
# file_path = os.path.join(base_path, 'r1.json')  # está na mesma pasta

# with open(file_path) as file:
#     data = json.load(file)

# print(data)

#Abaixo, ele usa o ''' para definir uma string JSON de multiplas linhas.
# router_json = ''' 
# {
#     "router": {
#         "hostname": "R1",
#         "interfaces": [
#             {
#                 "id": "0",
#                 "enabled": "true",
#                 "name": "GigabitEthernet0/0",
#                 "ip": "192.168.1.254",
#                 "mask": "255.255.255.0"
#             },
#             {
#                 "id": "1",
#                 "enabled": "true",
#                 "name": "GigabitEthernet0/1",
#                 "ip": "172.16.1.2",
#                 "mask": "255.255.255.0"
#             }
#         ],
#         "routing": {
#             "routes": [
#                 {
#                     "destination": "192.168.2.0",
#                     "mask": "255.255.255.0",
#                     "gateway": "192.168.1.253"
#                 },
#                 {
#                     "destination": "0.0.0.0",
#                     "mask": "0.0.0.0",
#                     "gateway": "201.1.113.54"
#                 }
#             ]
#         }
#     }
# }
# '''    

# data = json.loads(router_json)

router_dict = {
    "router": {
        "hostname": "R1",
        "interfaces": [
            {
                "id": "0",
                "enabled": "true",
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask": "255.255.255.0"
            },
            {
                "id": "1",
                "enabled": "true",
                "name": "GigabitEthernet0/1",
                "ip": "172.16.1.2",
                "mask": "255.255.255.0"
            }
        ],
        "routing": {
            "routes": [
                {
                    "destination": "192.168.2.0",
                    "mask": "255.255.255.0",
                    "gateway": "192.168.1.253"
                },
                {
                    "destination": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "201.1.113.54"
                }
            ]
        }
    }
}

router_json = json.dumps(router_dict)
print (router_json)