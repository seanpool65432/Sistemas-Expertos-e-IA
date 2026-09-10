def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return (c - x) / (c - b)
    return 0.0

conductores = [3, 6, 12]

for años in conductores:
    grados = {
        "Novato": membresia_triangular(años, 0, 0, 5),
        "Intermedio": membresia_triangular(años, 2, 5, 8),
        "Experto": membresia_triangular(años, 5, 10, 20)
    }
    
    mejor_categoria = max(grados, key=grados.get)
    
    print(f"Años de experiencia: {años}")
    print(grados)
    print(f"Categoría asignada: {mejor_categoria}\n")