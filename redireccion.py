"""
Ejercicio para redireccionar
Guillermo Labrador Vazquez
"""

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests
mySocket.listen(5)

try:
    while True:
        #numero aleatorio
        aleatorio = random.randint(11111, 9999999)

        url_aleatoria = "http://localhost:1234/" + str(aleatorio)

        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('HTTP request received:')
        print (recvSocket.recv(1024))

        htmlAnswer = """<html><head><meta http-equiv='refresh' content='2;
        url=http://localhost:1234/""" + str(aleatorio) + """'></head>
        <body> Nos redirecciona a """ + url_aleatoria + "</body></html>"

        recvSocket.send(bytes("HTTP/1.1 302 Found \r\n\r\n"
                        + htmlAnswer + "\r\n", 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print('Finishing connection...')
