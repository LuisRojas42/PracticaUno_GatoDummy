import socket

HOST = "10.100.70.104"
PORT = 54321
msgFromClient = "MENSAJE"
bufferSize = 1024
juego = True

while True:

    print("\n******GATO DUMMY*******")
    print ("1. Conectar")
    print ("2. Salir")
    opc = raw_input('')
    juego = True

    # CONECTA A SERVIDOR
    if opc == "1":
        print ("\n HOST:")
        HOST = raw_input('')
        print ("\n Puerto:")
        PORT = raw_input('')
    else:
        exit();
    # serverAddressPort = (HOST, int(PORT))
    serverAddressPort = ("10.100.70.104", 54321)

    # ENVIA DIFICULTAD
    while True:
        print ("\nDificultad:")
        print ("1. Principiante")
        print ("2. Avanzado")
        dificultad = raw_input('')
        if dificultad == "1" or dificultad == "2":
            break
        else:
            print ("\nIngrese una dificultad valida")
    bytesToSend = str.encode(dificultad)
    print ("\nINICIA")
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while juego:
        try:
            # RECIBE TABLERO
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
            msgFromServer = msgFromServer[0].encode("utf-8")
            print (msgFromServer)

            # ENVIA TIRO HASTA TERMINAR
            if msgFromServer == "ganaste":
                juego = False
            else:
                print ("\nTiro:")
                tiro = raw_input('')
                '''while True:
                    print ("\nTiro:")
                    tiro = raw_input('')
                     if (tiro[0] == "A" or tiro[0] == "B" or tiro[0] == "C") and (tiro[1] == "1" or tiro[1] == "2" or tiro[1] == "3"):
                        if dificultad == "1":
                            break
                        elif (tiro[0] == "A" or tiro[0] == "B" or tiro[0] == "C" or tiro[0] == "D" or tiro[0] == "E") and (tiro[1] == "1" or tiro[1] == "2" or tiro[1] == "3" or tiro[1] == "4" or tiro[1] == "5"):
                            break
                        else:
                            print ("\nIngrese un tiro valido")
                    else:
                        print ("\nIngrese un tiro valido")'''

                bytesToSend = str.encode(tiro)


        except:
            print ("No se pudo conectar al server")
            break;

    UDPClientSocket.close()