import tkinter as tk

app = tk.Tk()
app.geometry("500x550")
app.configure(background="Grey")
tk.Wm.wm_title(app, "Cifrado y Descifrado Vigenère (con Ñ)")

mensaje_sv = tk.StringVar(app)
clave_sv = tk.StringVar(app)
resultado_sv = tk.StringVar(app)

# Alfabeto de 27 letras incluyendo la Ñ
ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrado_vigenere(mensaje, clave, cifrar=True):
    if not clave:
        return mensaje

    resultado = ""
    clave = clave.upper()
    idx_clave = 0
    num_letras = len(ALFABETO)

    for char in mensaje:
        char_upper = char.upper()

        if char_upper in ALFABETO:
            # Índice de la letra del mensaje y de la clave en el alfabeto
            pos_msg = ALFABETO.index(char_upper)
            pos_clave = ALFABETO.index(clave[idx_clave % len(clave)].upper())

            if cifrar:
                nueva_pos = (pos_msg + pos_clave) % num_letras
            else:
                nueva_pos = (pos_msg - pos_clave) % num_letras

            letra_resultado = ALFABETO[nueva_pos]

            # Preserva si la letra original era minúscula o mayúscula
            if char.islower():
                resultado += letra_resultado.lower()
            else:
                resultado += letra_resultado

            idx_clave += 1
        else:
            # Los espacios, números y símbolos no avanzan el contador de la clave
            resultado += char

    return resultado

def procesar_cifrado():
    texto = mensaje_sv.get()
    clave = clave_sv.get()
    resultado_sv.set(cifrado_vigenere(texto, clave, cifrar=True))

def procesar_descifrado():
    texto = mensaje_sv.get()
    clave = clave_sv.get()
    resultado_sv.set(cifrado_vigenere(texto, clave, cifrar=False))

# Encabezado e Entradas de Texto
tk.Label(
    app,
    text="Ingrese el mensaje:",
    font=("Arial", 18),
    bg="Grey",
    fg="White",
).pack(expand=True)

tk.Entry(
    app,
    bg='White',
    fg='Black',
    font=('Arial', 18),
    justify='center',
    textvariable=mensaje_sv
).pack(expand=True)

tk.Label(
    app,
    text="Ingrese la palabra clave:",
    font=("Arial", 18),
    bg="Grey",
    fg="White",
).pack(expand=True)

tk.Entry(
    app,
    bg='White',
    fg='Black',
    font=('Arial', 18),
    justify='center',
    textvariable=clave_sv
).pack(expand=True)

# Marco (Frame) para agrupar los botones lado a lado
frame_botones = tk.Frame(app, bg="Grey")
frame_botones.pack(expand=True)

tk.Button(
    frame_botones,
    text='Cifrar',
    font=('Arial', 18, 'bold'),
    bg='#00FF00',
    width=12,
    command=procesar_cifrado
).pack(side=tk.LEFT, padx=10)

tk.Button(
    frame_botones,
    text='Descifrar',
    font=('Arial', 18, 'bold'),
    bg='#FF8C00',
    fg='white',
    width=12,
    command=procesar_descifrado
).pack(side=tk.LEFT, padx=10)

# Resultado
tk.Label(
    app,
    text="Resultado:",
    font=("Arial", 18),
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