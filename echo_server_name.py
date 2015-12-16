import socket
import sys

#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 10001)
print >>sys.stderr, 'Starting up on %s port %s' % server_address
sock.bind(server_address)
sock.listen(5)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'recived "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    except Exception, e:
        print type(e)
        print e
    finally:
        connection.close()
