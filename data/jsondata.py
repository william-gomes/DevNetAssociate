import os
import json

# Caminho absoluto do arquivo atual
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'r1.json')  # está na mesma pasta

with open(file_path) as file:
    data = json.load(file)

print(data)