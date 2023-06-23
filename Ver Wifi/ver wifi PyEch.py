import subprocess
import tkinter as tk
import os

nombre_archivo_png = "[PON TU IMAGEN]"
nombre_archivo_ico = "[PON TU ICONO]"

directorio_script = os.path.dirname(os.path.abspath(__file__))

ruta_archivo_png = os.path.join(directorio_script, nombre_archivo_png) if nombre_archivo_png else None

ruta_archivo_ico = os.path.join(directorio_script, nombre_archivo_ico) if nombre_archivo_ico else None

ventana = tk.Tk()
ventana.title("[TITULO DE LA VENTANA]")
ventana.geometry("400x300")

if ruta_archivo_png and os.path.isfile(ruta_archivo_png):

    imagen_fondo = tk.PhotoImage(file=ruta_archivo_png)
    imagen_fondo = imagen_fondo.subsample(2)

    etiqueta_fondo = tk.Label(ventana, image=imagen_fondo)
    etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

if ruta_archivo_ico and os.path.isfile(ruta_archivo_ico):

    ventana.iconbitmap(ruta_archivo_ico)

cuadro_detalles_wifi = tk.Text(ventana, bg="black", fg="green", font=("Courier", 12))
cuadro_detalles_wifi.pack(pady=20)

resultado = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("cp1252")

for linea in resultado.split("\n"):
    if "SSID" in linea and "BSSID" not in linea:
        nombre_red = linea.split(":")[1].strip()
        break
else:
    cuadro_detalles_wifi.insert(tk.END, "No se pudo encontrar el nombre de la red wifi a la que estás conectado.")
    ventana.mainloop()
    exit()

resultado = subprocess.check_output(["netsh", "wlan", "show", "profile", nombre_red, "key=clear"]).decode("cp1252")

detalles_wifi = ""

for linea in resultado.split("\n"):
    if "Contenido de la clave" in linea:
        contraseña = linea.split(":")[1].strip()
        detalles_wifi += f"Contraseña de tu wifi: {contraseña}"
    else:
        detalles_wifi += linea + "\n"

cuadro_detalles_wifi.insert(tk.END, detalles_wifi)

seccion_adicional = """  , __        ___       _     
 /|/  \      / (_)     | |    
  |___/      \__   __  | |    
  |    |   | /    /    |/ \   
  |     \_/|/\___/\___/|   |_/
          /|                  
          \|                """

cuadro_detalles_wifi.insert(tk.END, seccion_adicional)

ventana.mainloop()
