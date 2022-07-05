import socket
import threading
import time
# Choosing Nickname
nickname = input("Choose your nickname: ")
Disconnect = "bye"

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.5', 55553))
# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'CONNECTED!' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'CONNECTED!':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("Connection Ended!")
            break
    client.close()
# Sending Messages To Server
def write():
    count=0
    while True:
        message = '{}: {}'.format(nickname, input(''))
        if(message== '{}: {}'.format(nickname,Disconnect)):
            client.send('{} has left!'.format(nickname).encode('ascii'))
            client.close()
            break
        if(count==4):
            print("You have exceeded message limit, you can't send messages for the next 2 mins")
            time.sleep(120)
        client.send(message.encode('ascii'))
        count=count+1
        

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()