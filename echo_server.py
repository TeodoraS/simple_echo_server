import socket
import sys

#Creating TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bing the socket to the port and the server address(here, localhost)
server_address = ('127.0.0.1', 50018)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Listen for incoming connections
sock.listen(1)

while True:
    #Wait for a connection
    print >>sys.stderr, "waiting for a connection"
    connection, client_address = sock.accept() #returns an open connection
#between server and client along with the address of the client

    try:
        print sys.stderr, 'connection from', client_address

        #Recieve the data in small chunks and retransmit it
        while True:
            datas = []
            data = connection.recv(16)
            datas.append(data)
            print >>sys.stderr, 'recived "%s"' % data,
            if data:
                print >>sys.stderr, 'sending data back to client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
    
    finally:
        datas
        #Clean up the connection even in the event of n error
        connection.close()

    
