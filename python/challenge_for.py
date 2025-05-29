favorite_cars = [
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2022,
        "price": 79999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": True,
        "owner": None
    },
    {
        "make": "Porsche",
        "model": "911 Carrera",
        "year": 2023,
        "price": 106500.00,
        "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2022,
        "price": 27995.00,
        "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Chevrolet",
        "model": "Corvette",
        "year": 2023,
        "price": 62995.00,
        "features": ["Supercharged", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "R8",
        "year": 2023,
        "price": 144195.00,
        "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
        "is_electric": False,
        "owner": None
    }
]

for car in favorite_cars:
    try:
        if car["price"] > 100000.00:
            print("Encontrei um carro acima de 100.000,00")
            # print(f"{car['make']} {car['model']} {car['year']}")
            # print (f"Price: ${car['price']:.2f} a expensive car")
            print (car)
        # else:
        #     pass #Nao faz nada, apenas continua o loop
        #Aqui ou eu uso o else passando o pass para não fazer nada, ou eu nem uso o else já que o objetivo era apenas listar os carros que passem de 100.000,00.
    except TypeError as e:
        print("Error: Invalid data type encountered.")
        print (e)
    else:
        print("Carro abaixo de 100.000,00")
    finally:
        print("Processing next car...\n")
        # This block will always execute, regardless of whether an exception occurred or not

    
