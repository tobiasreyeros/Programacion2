from random import randint
lista_estudiantes=["Tobias","Joaquin","Federico","Santiago","Leon","Tomas","Mario"]
lista_oral=[]
num=0
limite=6
for i in range(len(lista_estudiantes)):
    num=randint(0,limite)
    print(lista_estudiantes[num])
    lista_oral.append(lista_estudiantes[num])
    del(lista_estudiantes[num])
    limite=limite-1
    
print("El alumno",lista_oral)