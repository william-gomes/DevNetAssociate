my_first_person = {
    "name": "William",
    "surname": "Gomes",
    "age": 31,
    "is_happy": True,
    "enemies": [None]
}

# print(my_first_person["surname"])  # This will raise a KeyError because 'surname' is not defined as a variable
#print(my_first_person["surname"],my_first_person["age"])  # This will print the surname and age of the person

my_second_person = {
    "name": "John",
    "surname": "Doe",
    "age": 25,
    "is_happy": False,
    "enemies": [my_first_person]
}
my_first_list = [my_first_person, my_second_person]

# print(my_first_list[0]["name"])  # This will print the name of the first person in the list
# print(my_first_list[1]["enemies"][0]["name"])  # This will print the name of the first person's enemy
print (my_first_list)