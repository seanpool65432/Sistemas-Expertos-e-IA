import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

X = np.array([
    [22, 5, 0],
    [25, 4, 1],
    [30, 2, 0],
    [35, 6, 5],
    [40, 1, 0],
    [45, 8, 10],
    [50, 3, 2],
    [55, 7, 8],
    [60, 2, 1],
    [65, 5, 15]
])

Y = np.array([
    0, 
    0, 
    0, 
    1, 
    0, 
    1, 
    0, 
    1, 
    0, 
    1
])

arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X, Y)

nombres = ["Edad", "Horas_Online", "Compras_Previas"]
reglas = export_text(arbol, feature_names=nombres)

print("Reglas generadas para Marketing:")
print(reglas)