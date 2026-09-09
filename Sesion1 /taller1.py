servidor = {
    "cpu": 45,
    "ram": 8,
    "temp": 85,
    "ventilador": False
}
def diagnosticar(datos):
    if datos["temp"] > 80 and datos["ventilador"] == False:
        return "Alerta: Temperatura alta y ventilador apagado"
    elif datos["cpu"] >= 90 or datos["ram"] < 2:
        return "Advertencia: Recursos al límite"
    else:
        return "Estado normal"
print(diagnosticar(servidor))
servidor["temp"] = 60
servidor["ventilador"] = True
servidor["cpu"] = 95
print(diagnosticar(servidor))
servidor["cpu"] = 40
servidor["ram"] = 16
print(diagnosticar(servidor)) 