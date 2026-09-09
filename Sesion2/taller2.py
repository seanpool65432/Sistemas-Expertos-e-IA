hechos = {
    "monto_mayor_5000": True,
    "pais_extranjero": True,
    "ip_sospechosa": True
}
reglas = [
    {
        "id": "R1",
        "condiciones": {"monto_mayor_5000": True},
        "conclusion": {"transaccion_inusual": True}
    },
    {
        "id": "R2",
        "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
        "conclusion": {"alerta_fraude": True}
    },
    {
        "id": "R3",
        "condiciones": {"ip_sospechosa": True},
        "conclusion": {"requiere_verificacion": True}
    },
    {
        "id": "R4",
        "condiciones": {"alerta_fraude": True, "requiere_verificacion": True},
        "conclusion": {"bloquear_tarjeta": True}
    }
]
nuevos = True
while nuevos:
    nuevos = False
    for regla in reglas:
        cumple = all(hechos.get(k) == v for k, v in regla["condiciones"].items())
        if cumple:
            for c, v in regla["conclusion"].items():
                if c not in hechos:
                    hechos[c] = v
                    nuevos = True
                    print(f"Disparando {regla['id']} - Nuevo hecho: {c}={v}")
print(hechos)