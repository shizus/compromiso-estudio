import tkinter as tk
import subprocess

def on_yes():
    subprocess.run(r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=valorant --launch-patchline=live', shell=True)
    root.destroy()

def on_no():
    root.destroy()

root = tk.Tk()
root.title("Recordatorio de Estudio")

label = tk.Label(root, text="¿Ya estudiaste 2 horas hoy?", font=("Arial", 14))
label.pack(pady=20)

button_yes = tk.Button(root, text="Sí", command=on_yes, font=("Arial", 12))
button_yes.pack(side=tk.LEFT, padx=20, pady=20)

button_no = tk.Button(root, text="No", command=on_no, font=("Arial", 12))
button_no.pack(side=tk.RIGHT, padx=20, pady=20)

root.mainloop()
