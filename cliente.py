import socket

SERVER_ADDRESS = "127.0.0.1"
SERVER_PORT = 9090

s = socket.socket()

s.connect((SERVER_ADDRESS, SERVER_PORT))
try:
    input = raw_input
except NameError:
    pass
print("Conectado al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        numero_uno = input("Escribe el primer número: ") # Solicita al usuario que ingrese dos números y los almacena en las variables 'numero_uno' y 'numero_dos'
        numero_dos = input("Escribe el segundo número: ")
    except EOFError:
        print("Finalizado por el usuario")
        break
    if not numero_uno or not numero_dos:    # Verifica si alguno de los números ingresados es vacío
        print("No se pueden enviar números vacíos")
        continue
    data = numero_uno + "," + numero_dos    # Concatena los dos números ingresados 
    data = data.encode()
    s.send(data)
    response = s.recv(51200)
    if not response:
        print("El servidor no respondió")
        break
    response = response.decode()

    print("Respuesta del servidor:", response)

s.close()
