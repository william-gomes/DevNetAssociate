from classes.my_classes import Car

my_car = Car(marca="Jeep", modelo="Compass", ano=2022, km=31500, condicao="Semi Novo", cor="Cinza") #Argumentos nomeados (como marca="Jeep") não dependem da ordem.
my_wife_car = Car("Honda", "City", 2013, 95000, "Usado", "Cinza Claro") #Argumentos posicionais (como "Honda") dependem da ordem. Se colocar o argumento errado, pode dar erro ou criar um objeto com atributos errados.
#Resumindo, escolha entre argumentos nomeados, é a melhor prática, pois é mais legível e menos propenso a erros.

# print(my_car) #Vai imprimir o objeto
# print (my_car.marca) #Vai imprimir o atributo marca do objeto
# print(my_car.__dict__) #Vai imprimir os atributos do objeto 

my_car.start() #Liga o carro
my_car.acelerar(50) #Acelera o carro
my_car.acelerar(30) #Acelera mais o carro
my_car.stop() #Desliga o carro

print("O script foi executado com sucesso.".upper()) #Chamando o método upper() da classe str para deixar a mensagem em maiúsculas.