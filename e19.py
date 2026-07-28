import tkinter as tk
import random

secreto=random.randint(1,20)
app=tk.Tk()
vidas=6
entrada=tk.StringVar(app)
VidasSV=tk.StringVar(app)
resultado=tk.StringVar(app)

def intentar():
    global vidas
    print("Entrada: "+ entrada.get())
    if(vidas<0):
        resultado.set("Te quedaste sin vidas,Reinicia la aplicacion para seguir jugando")
        return
    numero_ingresado=int(entrada.get())
    if(numero_ingresado<secreto):
        resultado.set("El número ingresado es muy bajo")
    if(numero_ingresado>secreto):
        resultado.set("El número ingresado es muy alto")
    if(numero_ingresado==secreto):
        resultado.set("Felicidades, ganaste el juego")
    VidasSV.set('Vidas: '+str(vidas))
    vidas=vidas-1

app.geometry("800x500")
app.configure(background='Grey')
tk.Wm.wm_title(app, "Adivina el número")

tk.Button(
    app,
    text='Adivina',
    font=('Arial', 14),
    bg='White',
    command=intentar
).pack(expand=True)


tk.Label(
    app,
    textvariable=VidasSV,
    font=('Arial', 18),
    bg='Grey',
    justify='center'
).pack(expand=True)

tk.Entry(
    app,
    bg='White',
    fg='Black',
    font=('Arial',14),
    justify='center',
    textvariable=entrada
).pack(expand=True)


tk.Label(
    app,
    textvariable=resultado,
    font=('Arial',17),
    bg='Green'
).pack(expand=True)

app.mainloop()
