SocketProgramming:- Making a chatroom using TCP connection

Explanation for Server Code:
In this program we are using client-server approach which means that we will have many clients and 
one common main server.
The clients themselves will not going to directly communicate to each other but via the central server.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
- socket.AF_INET is used to tell that we are using internet socket.
- socket.SOCK_STREAM indicates that we are using TCP and not UDP.
After defining our socket we bind the host and the port.
The function "broadcast" is used to send the message to the client in the list of clients.
The function "handle" forwards the message sent by 1 client to all the other clients connected to the 
server. If somehow an error occurs that client ends it's connection.
Once a client is connected it sends the string ‘CONNECTED!’ to it, which will tell the client that
its nickname is requested. Once a nickname is entered it appends the nickname to the lists nicknames and
ip address to clients. After that, we print and broadcast this information. 
Finally, we start a new thread that runs the previously implemented handling function for this particular client

Explanation for client code:
Instead of binding and listening it connects to the already existing server using "client.connect()"
The client will need 2 threads to be running at the same time.
- one to receive messages from server.
- one to send the messages to the server.

Output Screenshot:
https://github.com/varun872/SocketProgramming/blob/e33d8c043728a156061c54e0e43b6ad00ef00ad8/Output.png