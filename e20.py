import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry("500x500")
app.configure(background="Grey")
tk.Wm.wm_title(app, "Cifrado César")

# Variables de Tkinter
mensaje_sv = tk.StringVar(app)
desplazamiento_sv = tk.StringVar(app)
resultado_sv = tk.StringVar(app)


def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            # Determina la base según si es mayúscula o minúscula
            base = ord("A") if caracter.isupper() else ord("a")
            # Aplica la fórmula del cifrado César desplazando dentro del alfabeto (26 letras)
            nuevo_codigo = (ord(caracter) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo_codigo)
        else:
            # Conserva espacios, números y símbolos sin modificar
            resultado += caracter
    return resultado


def procesar_mensaje():
    texto = mensaje_sv.get()
    try:
        desplazamiento = int(desplazamiento_sv.get())
    except ValueError:
        messagebox.showerror(
            "Error de entrada",
            "Por favor, ingresa un número entero válido para el desplazamiento.",
        )
        return

    texto_procesado = cifrar_cesar(texto, desplazamiento)
    resultado_sv.set(texto_procesado)


# Componentes de la Interfaz Gráfica

# Etiqueta y entrada para el mensaje
tk.Label(
    app,
    text="Ingresa el mensaje:",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(pady=(10, 0))

tk.Entry(
    app,
    bg="White",
    fg="Black",
    font=("Arial", 14),
    justify="center",
    textvariable=mensaje_sv,
).pack(expand=True, fill="x", padx=20)

# Etiqueta y entrada para el desplazamiento
tk.Label(
    app,
    text="Desplazamiento (positivo o negativo):",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(pady=(10, 0))

tk.Entry(
    app,
    bg="White",
    fg="Black",
    font=("Arial", 14),
    justify="center",
    textvariable=desplazamiento_sv,
).pack(expand=True, fill="x", padx=20)

# Botón para procesar (Cifrar / Descifrar)
tk.Button(
    app,
    text="Procesar mensaje",
    font=("Arial", 14),
    bg="#00FF00",
    command=procesar_mensaje,
).pack(expand=True)

# Etiqueta para mostrar el resultado
tk.Label(
    app,
    text="Resultado:",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(pady=(10, 0))

tk.Label(
    app,
    textvariable=resultado_sv,
    font=("Arial", 14, "bold"),
    bg="White",
    fg="Black",
    wraplength=450,
).pack(expand=True, fill="x", padx=20, pady=(0, 20))

app.mainloop()