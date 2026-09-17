import numpy as np

def funcionEscalon(z):
    if z >= 0:
        return 1
    else:
        return 0

def perceptron(X, W, b):
    Z = np.dot(X, W) + b
    return funcionEscalon(Z)

pesos = np.array([
    1, 
    1
])
sesgo = -0.5
casosPrueba = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
for entradas in casosPrueba:
    resultado = perceptron(entradas, pesos, sesgo)
    print(f"Entrada: {entradas} -> Salida OR: {resultado}")