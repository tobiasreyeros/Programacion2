def cifrado(mensaje, desp):
    resultado = '' 
    
    for i in range(len(mensaje)):
        char = mensaje[i]

        if 'A' <= char <= 'Z':
            nueva_pos = (ord(char) - ord('A') + desp) % 26
            resultado += chr(nueva_pos + ord('A'))
        else:
            # Si hay espacios o números, se mantienen igual
            resultado += char
        
    print("Resultado:", resultado)

mensaje_usuario = input('Ingrese el mensaje: ')
desp = int(input('Ingrese el desplazamiento: '))

cifrado(mensaje_usuario, desp)