import tkinter as tk
import random

secreto=random.randint(1,20)
hp = 6
app = tk.Tk()
entrada = tk.StringVar(app)
hpSV = tk.StringVar(app).set("Vidas: " + str(hp))

def intentar():
    global hp
    print("Entrada: " + entrada.get())
    num=int(entrada.get())
    print(num + 1)
    hpSV.set("Vidas: " + str(hp))
    hp = hp - 1
    
app.geometry("400x500")
app.configure(background="black")
tk.Wm.wm_title(app, "Adivina el numero")

tk.Button(
    app,
    text="Adivina",
    bg="yellow",
    fg="blue",
    command=lambda: print("Hola que tal "+ entrada.get()),
    font=("Arial",14)).pack(
        #fill=tk.BOTH,
        #expand=True,
        )
tk.Label(
    app,
    text="Adivina el numero entre 1 y 20",
    #font=("Arial",18)
    bg="black",
    fg="white",
    justify="center"
).pack(
    #fill=tk.BOTH,
    #expand=True,
    )

tk.Label(
    app,
    text="Vidas:",
    #font=("Arial",18)
    bg="black",
    fg="white",
    justify="center"
).pack(
#     fill=tk.BOTH,
#     expand=True,
    )

tk.Entry(
    fg="White",
    bg="Black",
    justify="center",
    textvaariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True,
)
    
    


app.mainloop()

