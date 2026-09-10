grados = {
    "desempeno_pobre": 0.2,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.8,
    "antiguedad_corta": 0.3,
    "antiguedad_larga": 0.7
}

def calcular_bono(datos):
    r1 = max(datos["desempeno_pobre"], datos["antiguedad_corta"])
    r2 = datos["desempeno_promedio"]
    r3 = min(datos["desempeno_excelente"], datos["antiguedad_larga"])
    return {
        "Bono Bajo": r1,
        "Bono Medio": r2,
        "Bono Alto": r3
    }

resultado = calcular_bono(grados)
print("Activación de bonos:", resultado)

fuerza_final = max(0.4, 0.7)
print("Fuerza final teórica para Bono Alto:", fuerza_final)