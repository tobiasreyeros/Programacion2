import tkinter as tk
import random

secreto=random.randint(1,20)
hp = 6
app = tk.Tk()
entrada = tk.StringVar(app)
hpSV = tk.StringVar(app).set("Vidas: " + str(hp))
resultado = tk.StringVar(app)

def intentar():
    global hp, secreto
    print("Entrada: " + entrada.get())
    num=int(entrada.get())
    if(num < secreto):
        resultado.set("El número es muy bajo")
    if(num > secreto):
        resultado.set("El número es muy alto")
    if(num == secreto):
        resultado.set("Ganaste, adivinaste el número")
    print(num + 1)
    hpSV.set("Vidas: " + str(hp))
    hp = hp - 1
    
app.geometry("700x600")
app.configure(background="black")
tk.Wm.wm_title(app, "Adivina el numero")

tk.Label(
    app,
    text="Adivina el numero entre 1 y 20",
    font=("Arial",18),
    bg="black",
    fg="white",
    justify="center"
).pack(expand=True)
tk.Label(
    app,
    textvariable="Vidas:",
    font=("Arial",18),
    bg="black",
    fg="white",
    justify="center"
).pack(
    expand=True)
tk.Entry(
    app,
    font=("Arial",14),
    fg="White",
    bg="Black",
    justify="center",
    textvaariable=entrada
).pack(expand=True)
tk.Button(
    app,
    text="Adivina",
    bg="yellow",
    fg="blue",
    command=lambda: print("Hola que tal "+ entrada.get()),
    font=("Arial",14)).pack(expand=True)

app.mainloop()

