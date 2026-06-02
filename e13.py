mensaje = input('Ingrese el mensaje: ')
desp = int(input('Ingrese el desplazamiento: '))
resultado = ''

# Primer for: recorre cada carácter del mensaje
for i in range(len(mensaje)):
    char = mensaje[i]

    if 'A' <= char <= 'Z':
        nuevo_valor_ascii = ord(char)
        
        # (ord(char) - 65) nos da la posición de 0 a 25
        nueva_pos = (ord(char) - ord('A') + desp) % 26
        resultado += chr(nueva_pos + ord('A'))
    else:
        # Si hay espacios o números, los dejamos igual
        resultado += char
        
print("Resultado:", resultado)