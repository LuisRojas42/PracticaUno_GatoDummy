import socket
from random import randint

HOST = "192.168.100.233"
PORT = 54321
bufferSize = 1024
msgFromServer = ""
posiciones = ""
cont = 0
juego = True

try:

    # CREO E INICIO SOCKET
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((HOST, PORT))
    print("Server iniciado")

    while True:
        print(".")
        # RECIBE DIFICULTAD
        data, address = UDPServerSocket.recvfrom(bufferSize)
        data = data.decode("utf-8")
        print("Dificultad: ", data)
        if data == "1":
            m = n = k = 3
            msgFromServer = "\n---\n---\n---"
        elif data == "2":
            n = m = k = 5
            msgFromServer = "\n-----\n-----\n-----\n-----\n-----"

        # RESPONDE
        bytesToSend = str.encode(msgFromServer)
        UDPServerSocket.sendto(bytesToSend, address)

        # INICIA JUEGO
        while juego:

            print("..")
            # RECIVE TIRO
            tiro, address = UDPServerSocket.recvfrom(bufferSize)
            tiro = tiro.decode("utf-8")
            if n == 3:
                if tiro[0] == "A":
                    lugar = 4*(int(tiro[1])-1)+1
                if tiro[0] == "B":
                    lugar = 4*(int(tiro[1])-1)+2
                if tiro[0] == "C":
                    lugar = 4*(int(tiro[1])-1)+3
                if tiro[0] == "D":
                    lugar = 4*(int(tiro[1])-1)+4
                if tiro[0] == "E":
                    lugar = 4*(int(tiro[1])-1)+5
            else:
                if tiro[0] == "A":
                    lugar = 6*(int(tiro[1])-1)+1
                if tiro[0] == "B":
                    lugar = 6*(int(tiro[1])-1)+2
                if tiro[0] == "C":
                    lugar = 6*(int(tiro[1])-1)+3
                if tiro[0] == "D":
                    lugar = 6*(int(tiro[1])-1)+4
                if tiro[0] == "E":
                    lugar = 6*(int(tiro[1])-1)+5

            print("Tiro cliente: ", tiro)
            print("Lugar: ", lugar)

            # TIRO SERVIDOR
            tablero = ""
            aux = 0
            while True:
                if n == 3:
                    numran = randint(1, 3)
                    if numran == 1:
                        numran = randint(1, 3)
                    if numran == 2:
                        numran = randint(5, 7)
                    if numran == 3:
                        numran = randint(9, 11)
                    if numran != lugar:
                        if posiciones.find(str(numran)) < 0:
                            break
                else:
                    numran = randint(1, 5)
                    if numran == 1:
                        numran = randint(1, 5)
                    if numran == 2:
                        numran = randint(7, 11)
                    if numran == 3:
                        numran = randint(13, 17)
                    if numran == 4:
                        numran = randint(19, 23)
                    if numran == 5:
                        numran = randint(25, 29)
                    if numran != lugar:
                        if posiciones.find(str(numran)) < 0:
                            break
            print("Tiro Server:", numran)

            # NUEVO TABLERO
            for x in msgFromServer:
                if aux == lugar:
                    tablero = tablero + "x"
                    posiciones = posiciones + str(aux) + "-"
                elif aux == numran:
                    tablero = tablero + "o"
                    posiciones = posiciones + str(aux) + "-"
                else:
                    tablero = tablero + x
                aux = aux+1
            msgFromServer = tablero

            # CONDICIONES DE GANE
            if n == 3:
                if msgFromServer[1] == msgFromServer[2] and msgFromServer[2] == msgFromServer[3] and msgFromServer[1] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[5] == msgFromServer[6] and msgFromServer[6] == msgFromServer[7] and msgFromServer[5] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[9] == msgFromServer[10] and msgFromServer[10] == msgFromServer[11] and msgFromServer[9] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[1] == msgFromServer[5] and msgFromServer[5] == msgFromServer[9] and msgFromServer[1] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[2] == msgFromServer[6] and msgFromServer[6] == msgFromServer[10] and msgFromServer[2] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[3] == msgFromServer[7] and msgFromServer[7] == msgFromServer[11] and msgFromServer[3] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
            else:
                print("5")
                if msgFromServer[1:6].find("xxxxx") >= 0 \
                        or msgFromServer[7:12].find("xxxxx") >= 0 \
                        or msgFromServer[13:18].find("xxxxx") >= 0 \
                        or msgFromServer[19:24].find("xxxxx") >= 0 \
                        or msgFromServer[25:30].find("xxxxx") >= 0:
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break
                if msgFromServer[1] == msgFromServer[7] \
                    and msgFromServer[7] == msgFromServer[13] \
                        and msgFromServer[13] == msgFromServer[19] \
                        and msgFromServer[19] == msgFromServer[25] \
                        and msgFromServer[1] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break

                if msgFromServer[2] == msgFromServer[8] \
                    and msgFromServer[8] == msgFromServer[14] \
                        and msgFromServer[14] == msgFromServer[20] \
                        and msgFromServer[20] == msgFromServer[26] \
                        and msgFromServer[2] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break

                if msgFromServer[3] == msgFromServer[9] \
                    and msgFromServer[9] == msgFromServer[15] \
                        and msgFromServer[15] == msgFromServer[21] \
                        and msgFromServer[21] == msgFromServer[27] \
                        and msgFromServer[3] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break

                if msgFromServer[4] == msgFromServer[10] \
                    and msgFromServer[10] == msgFromServer[16] \
                        and msgFromServer[16] == msgFromServer[22] \
                        and msgFromServer[22] == msgFromServer[28] \
                        and msgFromServer[4] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break

                if msgFromServer[5] == msgFromServer[11] \
                    and msgFromServer[11] == msgFromServer[17] \
                        and msgFromServer[17] == msgFromServer[23] \
                        and msgFromServer[23] == msgFromServer[29] \
                        and msgFromServer[29] != "-":
                    msgFromServer = "ganaste"
                    bytesToSend = str.encode(msgFromServer)
                    UDPServerSocket.sendto(bytesToSend, address)
                    break

            print(posiciones, "\n")
            bytesToSend = str.encode(msgFromServer)
            UDPServerSocket.sendto(bytesToSend, address)

        print("fin")
        posiciones = ""
        msgFromServer = ""

    UDPServerSocket.close()
except:
    print("error")