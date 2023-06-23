import subprocess

resultado = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("cp1252")

for linea in resultado.split("\n"):
    if "SSID" in linea and "BSSID" not in linea:
        nombre_red = linea.split(":")[1].strip()
        break
else:
    print("No se pudo encontrar el nombre de la red wifi a la que estás conectado.")
    exit()

resultado = subprocess.check_output(["netsh", "wlan", "show", "profile", nombre_red, "key=clear"]).decode("cp1252")

print(resultado)
