import requests

base_url = "https://swapi.py4e.com/api/"
endpoint = "people/"
# Response object
response = requests.get(base_url + endpoint)
#print (response)

# print ("Textual response:")
# # print(response.text)
# print("Json:")
# print(response.json())
# print("Status Code:")
# print (response.status_code)
# print("Headers:")
# print (response.headers)

data = response.json()
#print(data['results'][0]['name'])

# Print names of all people in the response
print("Names of all people in the response:")
for person in data['results']:
    print(f"Name: {person['name']} - Height: {person['height']} - Gender: {person['gender']}")