import requests

base_url = "https://swapi.py4e.com/api/"
endpoint = "people/"
# Response object
response = requests.get(base_url + endpoint)

data = response.json()
encontrada = False

# Print names of all people in the response
print("Procurando a Leia na resposta:")
for person in data['results']:
    if person['name'] == "Leia Organa":
        #print(f"Name: {person['name']} - Height: {person['height']} - Gender: {person['gender']}")
        print("Leia Organa encontrada! Segue os dados dela:")
        print(person)
        encontrada = True
        break
    else:
        print("Leia Organa não encontrada na resposta, procurando na próxima página...")

if not encontrada:
    print("Leia Organa não encontrada em nenhuma das páginas.")