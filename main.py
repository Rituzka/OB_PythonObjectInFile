import pickle


class Vehiculo:
    marca = ""
    velocidad = 0.0
    color = ""

    def __init__(self, marca, velocidad, color):
        self.marca = marca
        self.velocidad = velocidad
        self.color = color


v1 = Vehiculo('Peugeot', 150.00, 'Rojo')
file = open('datos.bin', 'wb')
pickle.dump(v1, file)
file.close()

file = open('datos.bin', 'rb')
v1 = pickle.load(file)
file.close()
