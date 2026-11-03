import os
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

# Establecer la carpeta de trabajo donde se ubica el script
directorio_script = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_script)

pygame.mixer.init()

try:
    pygame.mixer.music.load("musica_fondo.mp3")
    pygame.mixer.music.play(-1)  # -1 para reproducción en bucle
    
    sonido_victoria = pygame.mixer.Sound("victoria.wav")
    sonido_derrota = pygame.mixer.Sound("derrota.wav")
    sonido_empate = pygame.mixer.Sound("empate.wav")
except Exception as e:
    print("Nota: No se encontraron algunos archivos de audio. El juego funcionará sin sonido.")

root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("450x550")
root.resizable(False, False)
root.config(bg="#2C3E50")

puntos_jugador = 0
puntos_maquina = 0

opciones = ["Piedra", "Papel", "Tijera"]

def jugar(eleccion_jugador):
    global puntos_jugador, puntos_maquina
    
    eleccion_maquina = random.choice(opciones)
    
    if eleccion_jugador == eleccion_maquina:
        resultado = "¡Es un Empate!"
        color_resultado = "#F39C12"
        try: sonido_empate.play()
        except: pass

    elif (eleccion_jugador == "Piedra" and eleccion_maquina == "Tijera") or \
         (eleccion_jugador == "Papel" and eleccion_maquina == "Piedra") or \
         (eleccion_jugador == "Tijera" and eleccion_maquina == "Papel"):
        resultado = "¡Ganaste esta ronda!"
        color_resultado = "#2ECC71"
        puntos_jugador += 1
        try: sonido_victoria.play()
        except: pass

    else:
        resultado = "¡La Máquina gana!"
        color_resultado = "#E74C3C"
        puntos_maquina += 1
        try: sonido_derrota.play()
        except: pass

    lbl_eleccion_jugador.config(text=f"Tú elegiste: {eleccion_jugador}")
    lbl_eleccion_maquina.config(text=f"Máquina eligió: {eleccion_maquina}")
    lbl_resultado.config(text=resultado, fg=color_resultado)
    lbl_marcador.config(text=f"Tú: {puntos_jugador}  |  Máquina: {puntos_maquina}")

def reiniciar_juego():
    global puntos_jugador, puntos_maquina
    puntos_jugador = 0
    puntos_maquina = 0
    lbl_marcador.config(text="Tú: 0  |  Máquina: 0")
    lbl_eleccion_jugador.config(text="Tú elegiste: -")
    lbl_eleccion_maquina.config(text="Máquina eligió: -")
    lbl_resultado.config(text="¡Elige tu jugada!", fg="#ECF0F1")

# Cargar y redimensionar imágenes de forma uniforme
TAM_BOTON = (100, 100)
try:
    img_p_raw = Image.open("piedra.png").resize(TAM_BOTON, Image.Resampling.LANCZOS)
    img_pa_raw = Image.open("papel.png").resize(TAM_BOTON, Image.Resampling.LANCZOS)
    img_t_raw = Image.open("tijera.png").resize(TAM_BOTON, Image.Resampling.LANCZOS)

    img_piedra = ImageTk.PhotoImage(img_p_raw)
    img_papel = ImageTk.PhotoImage(img_pa_raw)
    img_tijera = ImageTk.PhotoImage(img_t_raw)
    usar_imagenes = True
except Exception as e:
    print(f"No se pudieron cargar las imágenes con PIL: {e}")
    usar_imagenes = False


lbl_titulo = tk.Label(
    root, 
    text="PIEDRA, PAPEL O TIJERA", 
    font=("Helvetica", 16, "bold"), 
    bg="#2C3E50", 
    fg="#ECF0F1"
)
lbl_titulo.pack(pady=15)

lbl_marcador = tk.Label(
    root, 
    text="Tú: 0  |  Máquina: 0", 
    font=("Helvetica", 14, "bold"), 
    bg="#34495E", 
    fg="#F1C40F", 
    padx=20, 
    pady=8
)
lbl_marcador.pack(pady=10)

lbl_eleccion_jugador = tk.Label(root, text="Tú elegiste: -", font=("Helvetica", 11), bg="#2C3E50", fg="#ECF0F1")
lbl_eleccion_jugador.pack(pady=2)

lbl_eleccion_maquina = tk.Label(root, text="Máquina eligió: -", font=("Helvetica", 11), bg="#2C3E50", fg="#ECF0F1")
lbl_eleccion_maquina.pack(pady=2)

lbl_resultado = tk.Label(
    root, 
    text="¡Elige tu jugada!", 
    font=("Helvetica", 14, "bold"), 
    bg="#2C3E50", 
    fg="#ECF0F1"
)
lbl_resultado.pack(pady=15)

frame_botones = tk.Frame(root, bg="#2C3E50")
frame_botones.pack(pady=20)

if usar_imagenes:
    btn_piedra = tk.Button(frame_botones, image=img_piedra, command=lambda: jugar("Piedra"), bg="#34495E", activebackground="#1ABC9C", bd=2, relief="groove")
    btn_papel = tk.Button(frame_botones, image=img_papel, command=lambda: jugar("Papel"), bg="#34495E", activebackground="#1ABC9C", bd=2, relief="groove")
    btn_tijera = tk.Button(frame_botones, image=img_tijera, command=lambda: jugar("Tijera"), bg="#34495E", activebackground="#1ABC9C", bd=2, relief="groove")
else:
    btn_piedra = tk.Button(frame_botones, text="🪨\nPiedra", font=("Helvetica", 12, "bold"), width=8, height=3, command=lambda: jugar("Piedra"), bg="#34495E", fg="white")
    btn_papel = tk.Button(frame_botones, text="📄\nPapel", font=("Helvetica", 12, "bold"), width=8, height=3, command=lambda: jugar("Papel"), bg="#34495E", fg="white")
    btn_tijera = tk.Button(frame_botones, text="✂️\nTijera", font=("Helvetica", 12, "bold"), width=8, height=3, command=lambda: jugar("Tijera"), bg="#34495E", fg="white")

btn_piedra.grid(row=0, column=0, padx=10)
btn_papel.grid(row=0, column=1, padx=10)
btn_tijera.grid(row=0, column=2, padx=10)


btn_reiniciar = tk.Button(
    root, 
    text="Reiniciar Puntuación", 
    font=("Helvetica", 10, "bold"), 
    command=reiniciar_juego, 
    bg="#E74C3C", 
    fg="white", 
    padx=10, 
    pady=5
)
btn_reiniciar.pack(pady=20)

root.mainloop()
