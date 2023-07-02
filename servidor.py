import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 9090

s = socket.socket()

s.bind((SERVER_ADDRESS, SERVER_PORT))
s.listen(13)
print("Escuchando al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    c, addr = s.accept()
    while True:
        data = c.recv(2048)
        if not data:
            print("Fin de la transmisión desde el cliente")
            break
        data = data.decode()
        print("Información recibida desde el cliente: " + data)   # Imprime la información recibida desde el cliente

        numeros = data.split(",")        # Separa los números enviados 
        if len(numeros) != 2:
            response = "Error: Se esperaban dos números separados por coma"  # Verificaciòn si se enviaron dos números correctamente
        else:
            try:
                numero_uno = float(numeros[0])
                numero_dos = float(numeros[1])
                resultado = numero_uno + numero_dos    # guarda el resultado en la variable 'response'
                response = "La suma es: " + str(resultado)
            except ValueError:
                response = "Los valores enviados no son números enteros"
        response = response.encode()
        c.send(response)
    
    c.close()
 
