from classes.my_classes import Person

my_person = Person(first_name="João", last_name="Silva", age=30, height=1.75, is_happy=False)  # Argumentos nomeados
my_person2 = Person(first_name="João", last_name="Silva", age=30, height=1.75)

my_person.introduce()  # Chama o método introduce da classe Person
my_person2.introduce()  # Chama o método introduce da classe Person