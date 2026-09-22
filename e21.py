import os
import sys
from tkinter import *
from tkinter import messagebox, ttk

# DICCIONARIO CON TODAS LAS CONVERSIONES Y SUS FÓRMULAS
CATEGORIAS = {
    "Longitud": {
        "m a km": lambda x: x / 1000,
        "m a millas": lambda x: x / 1609.34,
        "cm a pulgadas": lambda x: x / 2.54,
        "m a pies": lambda x: x * 3.28084,
    },
    "Temperatura": {
        "Celsius a Fahrenheit": lambda x: (x * 9 / 5) + 32,
        "Celsius a Kelvin": lambda x: x + 273.15,
        "Fahrenheit a Kelvin": lambda x: (x - 32) * 5 / 9 + 273.15,
    },
    "Masa": {
        "Kg a Libra": lambda x: x * 2.20462,
        "Gr a Onzas": lambda x: x / 28.3495,
        "Tonelada a Kg": lambda x: x * 1000,
    },
    "Velocidad": {
        "Km/h a Mph": lambda x: x / 1.60934,
        "Km/h a m/s": lambda x: x / 3.6,
        "Km/h a nudos": lambda x: x / 1.852,
    },
    "Volumen": {
        "Litros a galones": lambda x: x / 3.78541,
        "Litros a pies cúbicos": lambda x: x / 28.3168,
    },
    "Monedas": {
        "Pesos a Dólares": lambda x: x / 1000,
        "Pesos a Reales": lambda x: x / 200,
        "Pesos a Euros": lambda x: x / 1100,
    },
    "Informática": {
        "B a KB": lambda x: x / 1024,
        "B a MB": lambda x: x / (1024**2),
        "B a GB": lambda x: x / (1024**3),
        "B a TB": lambda x: x / (1024**4),
    },
}


# Función para obtener la ruta absoluta de recursos (soporta ejecución normal y .exe empaquetado)
def obtener_ruta_recurso(ruta_relativa):
    try:
        ruta_base = sys._MEIPASS
    except Exception:
        ruta_base = os.path.abspath(".")
    return os.path.join(ruta_base, ruta_relativa)


# ------------ INTERFAZ TKINTER ------------
ventana = Tk()
ventana.title("Conversor de Unidades")
ventana.geometry("300x350")
ventana.resizable(0, 0)
ventana.config(bd=10)

Label(
    ventana,
    text="CONVERSOR DE UNIDADES",
    fg="black",
    font=("Arial", 15, "bold"),
    padx=5,
    pady=5,
).grid(row=0, column=0, columnspan=2)

# Imagen opcional
try:
    from PIL import Image, ImageTk

    ruta_imagen = obtener_ruta_recurso("xd.jpg")
    imagen_conversor = Image.open(ruta_imagen)
    nueva_imagen = imagen_conversor.resize((125, 84))
    render = ImageTk.PhotoImage(nueva_imagen)
    label_imagen = Label(ventana, image=render)
    label_imagen.image = render
    label_imagen.grid(row=1, column=0, columnspan=2)
except Exception:
    Label(ventana, text="[Imagen no encontrada]").grid(
        row=1, column=0, columnspan=2
    )

# Variables de control
categoria_seleccionada = StringVar(ventana)
conversion_seleccionada = StringVar(ventana)
valor_input = StringVar(ventana)
resultado_var = StringVar(ventana, value="Resultado: -")

# Lista de categorías disponibles
lista_categorias = list(CATEGORIAS.keys())
categoria_seleccionada.set(lista_categorias[0])


# Función para actualizar las opciones del ComboBox al cambiar la categoría en OptionMenu
def actualizar_conversiones(*args):
    categoria = categoria_seleccionada.get()
    opciones = list(CATEGORIAS[categoria].keys())
    combo_conversion["values"] = opciones
    conversion_seleccionada.set(opciones[0])


# Menú desplegable para seleccionar CATEGORÍA (OptionMenu)
Label(
    ventana, text="Categoría:", fg="black", font=("Arial", 10, "bold")
).grid(row=2, column=0, pady=5)

menu_categorias = OptionMenu(
    ventana, categoria_seleccionada, *lista_categorias
)
menu_categorias.config(width=26)
menu_categorias.grid(row=2, column=1, pady=5)

# Menú desplegable para seleccionar CONVERSIÓN (ComboBox)
Label(
    ventana, text="Conversión:", fg="black", font=("Arial", 10, "bold")
).grid(row=3, column=0, pady=5)

combo_conversion = ttk.Combobox(
    ventana,
    textvariable=conversion_seleccionada,
    state="readonly",
    width=28,
)
combo_conversion.grid(row=3, column=1, pady=5)

# Se ejecuta al cambiar la categoría para sincronizar el ComboBox
categoria_seleccionada.trace_add("write", actualizar_conversiones)

# Campo de entrada de texto (Entry) para inputear el VALOR a convertir
Label(
    ventana, text="Valor:", fg="black", font=("Arial", 10, "bold")
).grid(row=4, column=0, pady=5)

entry_valor = Entry(ventana, textvariable=valor_input, width=32)
entry_valor.grid(row=4, column=1, pady=5)


# ------------ LÓGICA DE CONVERSIÓN ------------
def realizar_conversion():
    valor_texto = valor_input.get().strip()

    if not valor_texto:
        messagebox.showwarning(
            "Campo vacío", "Por favor, ingrese un número para convertir."
        )
        return

    try:
        valor = float(valor_texto)
        cat = categoria_seleccionada.get()
        conv = conversion_seleccionada.get()

        # Obtener la función lambda correspondiente y calcular
        funcion_conversion = CATEGORIAS[cat][conv]
        resultado = funcion_conversion(valor)

        # Si el resultado es muy pequeño, muestra más decimales o notación científica
        if resultado < 0.000001 and resultado > 0:
            resultado_var.set(f"Resultado: {resultado:.8e}")
        else:
            resultado_var.set(f"Resultado: {resultado:.8f}".rstrip('0').rstrip('.'))

    except ValueError:
        messagebox.showerror(
            "Error de Entrada", "Por favor, ingrese un valor numérico válido."
        )
    except Exception as e:
        messagebox.showerror(
            "Error", f"Ocurrió un error inesperado.\nDetalle: {e}"
        )


# Label para mostrar el Resultado
Label(
    ventana,
    textvariable=resultado_var,
    fg="blue",
    font=("Arial", 12, "bold"),
    pady=10,
).grid(row=5, column=0, columnspan=2)

# ------------ BOTÓN ------------
Button(
    ventana,
    text="CONVERTIR",
    command=realizar_conversion,
    height=2,
    width=12,
    bg="black",
    fg="white",
    font=("Arial", 10, "bold"),
).grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Inicializar las opciones del ComboBox la primera vez
actualizar_conversiones()

ventana.mainloop()