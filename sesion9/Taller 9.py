import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_entrenamiento = np.array([
    [20, 30, 0],
    [40, 50, 2],
    [35, 45, 1],
    [22, 25, 0],
    [45, 60, 3],
    [50, 70, 2],
    [28, 35, 0],
    [38, 48, 1],
    [33, 40, 1],
    [60, 85, 4]
])
Y_entrenamiento = np.array([
    0, 
    1, 
    1, 
    0, 
    1, 
    1, 
    0, 
    1, 
    1, 
    1
])

nuevo_cliente = np.array([[30, 40, 0]])

modelo_knn_1 = KNeighborsClassifier(n_neighbors=1)
modelo_knn_1.fit(X_entrenamiento, Y_entrenamiento)
print("Predicción con K=1:", modelo_knn_1.predict(nuevo_cliente)[0])

modelo_knn_5 = KNeighborsClassifier(n_neighbors=5)
modelo_knn_5.fit(X_entrenamiento, Y_entrenamiento)
print("Predicción con K=5:", modelo_knn_5.predict(nuevo_cliente)[0])