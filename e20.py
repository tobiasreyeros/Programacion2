import tkinter as tk

app = tk.Tk()
app.geometry("500x500")
app.configure(background="Grey")
tk.Wm.wm_title(app, "Cifrado César")

mensaje_sv = tk.StringVar(app)
desplazamiento_sv = tk.StringVar(app)
resultado_sv = tk.StringVar(app)

def cifrado(mensaje, desplazamiento):
    resultado = ""

    for i in range(len(mensaje)):
        char = mensaje[i]

        if "A" <= char <= "Z":
            nueva_pos = (ord(char) - ord("A") + desplazamiento) % 26
            resultado += chr(nueva_pos + ord("A"))
        elif "a" <= char <= "z":
            nueva_pos = (ord(char) - ord("a") + desplazamiento) % 26
            resultado += chr(nueva_pos + ord("a"))
        else:
            # Espacios, números y símbolos se mantienen igual
            resultado += char

    return resultado
    
def procesar_mensaje():
    texto = mensaje_sv.get()
    desplazamiento = int(desplazamiento_sv.get())
    
    texto_procesado = cifrado(texto, desplazamiento)
    resultado_sv.set(texto_procesado)

tk.Button(
    app,
    text='Cifrar',
    font=('Arial', 14),
    bg='#00FF00',
    command=procesar_mensaje
).pack(expand=True)

tk.Label(
    app,
    text="Ingrese el mensaje:",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(expand=True)

tk.Entry(
    app,
    bg='White',
    fg='Black',
    font=('Arial',14),
    justify='center',
    textvariable=mensaje_sv
).pack(expand=True)

tk.Label(
    app,
    text="Ingrese el desplazamiento:",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(expand=True)

tk.Entry(
    app,
    bg='White',
    fg='Black',
    font=('Arial',14),
    justify='center',
    textvariable=desplazamiento_sv
).pack(expand=True)

tk.Label(
    app,
    text="Mensaje cifrado:",
    font=("Arial", 12),
    bg="Grey",
    fg="White",
).pack(expand=True)

tk.Label(
    app,
    textvariable=resultado_sv,
    font=('Arial', 18),
    bg='White',
    justify='center'
).pack(expand=True)

app.mainloop()