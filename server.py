import socket
import threading
# Connection Data
host = '192.168.1.5'
#host = '10.20.206.121'
port = 55553

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
# Sending Messages To All Connected Clients
def broadcast(message,connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
            
# Handling Messages From Clients
def handle(client):
    count=1
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            if(count==5):
                client.send('{} has left!'.format(nickname).encode('ascii'))
                
            broadcast(message,client)
            count=count+1
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            # broadcast('{} left!'.format(nickname).encode('ascii'),client)
            nicknames.remove(nickname)
            break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('CONNECTED!'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'),client)
        print(end='\n')
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
receive()        