class Car:
    def __init__(self, marca: str, modelo: str, ano: int, km: int, condicao: str, cor: str) -> None:
        #atributos obrigatórios
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = km
        self.condicao = condicao
        self.cor = cor
        # Atributos opcionais
        self.ligado = False
        self.velocidade = 0

    def start(self) -> None:
        if self.ligado:
            print(f"{self.marca} {self.modelo} já está ligado.")
            return
        else:
            self.ligado = True
            print (f"{self.marca} {self.modelo} está ligado.")
    def stop(self) -> None:
        if not self.ligado:
            print(f"{self.marca} {self.modelo} já está desligado.")
            return
        else:
            self.ligado = False
            print (f"{self.marca} {self.modelo} está desligado.")    
    def acelerar(self, velocidade: int) -> None:
        if not self.ligado:
            print(f"{self.marca} {self.modelo} precisa estar ligado para acelerar.")
            return
        else:
            self.velocidade += velocidade
            print(f"{self.marca} {self.modelo} acelerou para {self.velocidade} km/h.")