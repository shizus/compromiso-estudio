import tkinter as tk
from tkinter import messagebox
import subprocess
import json

file = open('settings.json', encoding='utf8')
settings = json.load(file)

def center_window(window, width_percentage=0.25, height_percentage=0.25):
    window.update_idletasks()
    width = int(window.winfo_screenwidth() * width_percentage)
    height = int(window.winfo_screenheight() * height_percentage)
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def on_yes():
    def check_confirmation(event=None):
        if entry.get() == settings["message"][1]:
            cmd = rf'"{settings["exe_path"]}"'

            if settings["riot_game_args"]["launch_product"] != "":
                cmd = cmd + f'--launch-product={settings["riot_game_args"]["launch_product"]} --launch-patchline=live'
            elif settings["steam_game_args"]["app_id"] != "":
                cmd = cmd + f' -applaunch {settings["steam_game_args"]["app_id"]}'
                
            subprocess.run(cmd, shell=True)
            confirmation_window.destroy()
            root.destroy()
        else:
            messagebox.showerror("Error", "La frase está mal escrita. Intenta de nuevo.")

    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Confirmación")

    label = tk.Label(confirmation_window, text=f"Ok, confirmá escribiendo la frase:\n{settings['message'][1]}", font=("Arial", 12))
    label.pack(pady=10)

    entry = tk.Entry(confirmation_window, font=("Arial", 12))
    entry.pack(pady=5)
    entry.bind("<Return>", check_confirmation)  # Asocia la tecla Enter con la función de confirmación

    button_confirm = tk.Button(confirmation_window, text="Confirmar", command=check_confirmation, font=("Arial", 12))
    button_confirm.pack(pady=10)

    center_window(confirmation_window, 0.5, 0.3)  # Ajusta el tamaño y centra la ventana

def on_no():
    root.destroy()

root = tk.Tk()
root.title("Recordatorio de Estudio")

label = tk.Label(root, text=settings["message"][0], font=("Arial", 14))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

button_yes = tk.Button(button_frame, text="Sí", command=on_yes, font=("Arial", 12))
button_yes.pack(side=tk.LEFT, padx=50)  # Espaciado de 50px entre los botones

button_no = tk.Button(button_frame, text="No", command=on_no, font=("Arial", 12))
button_no.pack(side=tk.RIGHT, padx=50)  # Espaciado de 50px entre los botones

center_window(root, 0.5, 0.3)  # Ajusta el tamaño y centra la ventana principal

root.mainloop()
