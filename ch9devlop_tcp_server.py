#devloping a tcp server and understaning sockets
#socket - is a internal end point for sending and revieing data.
#usign socket module.
#socketfamily -- AF_INET - is used to specific the protocol that will be used for communication.either ip4 or ip6, not tcp and udp.
#sockettype- either sock stream or sock dgram -depends on type connection ur using.
 #like sock stream - will mean ur specifying connection oriented protocol like TCP ,3-way handshake
 #sock dgram - will mean vr specifying connectionless -UDP
 #gethostname- it will get he hostname addresss and store it
 #bind method - allow us to bind the host and the port to the  socket .
 #while all of this is true then establish a connection
 #listen function  - start tcp listener,here v can specific how many computers can listen at a time.

 #accept method - accept the incoming tcp client information
 
 #send function - send  a msg over tcp
 #recive method - revieve tcp msgs over 
 #close method - allows to close the socket ,thus ending the connection.
 # % allows us to covert into certain data types

#!/usr/bin/python3

import socket

#serversocket object created ,which called socket fu
serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host=socket.gethostname()#GETTING THE IP ADDRESSS
port=444

#v now need to bind the object the values v got, host will be replaced/substitued by IP
serversocket.bind((host,port))

#starting TCP listener
serversocket.listen(3) 

while True: 
    clientsocket,address = serversocket.accept()#this will accept the THAT information coming from the client.

    print('Received connection from: %r '% str(address))

    message = 'thankyou for connecting to the server' + '\r\n'
    clientsocket.send(message.encode('ascii')) #v have encoded the msg 

    clientsocket.close()


 

