import json
import yaml
import xmltodict

with open('data/challenge_cars.json') as file:
    json_data = json.load(file)


for carro in json_data["cadastro_carro"]:
    print(carro["marca"], carro["modelo"], carro["ano"])

with open ('data/challenge_cars.yaml') as file:
    yaml_data = yaml.safe_load(file)

for carro in yaml_data["cadastro_carro"]:
    print(carro['car']['marca'], carro['car']['modelo'], carro['car']['ano']) #Como la a chave 'car' é um dicionário, é necessário acessar os valores com a chave 'marca', 'modelo' e 'ano'.

with open ('data/challenge_cars.xml') as file:
    xml_data = xmltodict.parse(file.read())

for carro in xml_data['cadastro_carro']['car']: # A chave 'car' é uma lista de dicionários, então é necessário iterar sobre ela.
    print(carro['make'], carro['model'], carro['year'])



