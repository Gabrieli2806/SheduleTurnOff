import os
import time
from tkinter import Tk, Entry, Button

# Función para cancelar el apagado programado
def cancel_shutdown():
    os.system("shutdown /a")

# Función para programar un apagado
def schedule_shutdown(minutes):
    # Programa el apagado en los minutos dados
    os.system(f"shutdown /s /t {minutes * 60}")

# Inicializa la interfaz gráfica de usuario (GUI) de Python
root = Tk()
root.title("Programar apagado")

# Crea un entry para introducir los minutos
entry = Entry(root, width=5)
entry.pack()

# Crea un botón para programar el apagado
button = Button(root, text="Programar apagado", command=lambda: schedule_shutdown(int(entry.get())))
button.pack()

# Crea un botón para cancelar el apagado programado
cancel_button = Button(root, text="Cancelar apagado", command=cancel_shutdown)
cancel_button.pack()

# Ejecuta el loop principal de la GUI
root.mainloop()
