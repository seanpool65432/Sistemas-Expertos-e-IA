import numpy as np
import skfuzzy as fuzz

def calcular_cog(x, mu):
    numerador = np.sum(x * mu)
    denominador = np.sum(mu)
    return numerador / denominador if denominador != 0 else 0

x_taller = np.array([
    10, 
    20, 
    30, 
    40
])

mu_taller = np.array([
    0.2, 
    0.8, 
    0.8, 
    0.0
])

resultado_manual = calcular_cog(x_taller, mu_taller)
print(f"Descuento exacto: {resultado_manual:.2f}%")

x_frenado = np.arange(0, 101, 1)
curva_gauss = fuzz.gaussmf(x_frenado, mean=70, sigma=10)
fuerza_frenado_crisp = fuzz.defuzz(x_frenado, curva_gauss, 'centroid')
print(f"Fuerza de frenado: {fuerza_frenado_crisp:.2f} Newtons")
