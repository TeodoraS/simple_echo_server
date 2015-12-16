import socket
import sys

def get_constants(prefix):
    """Create a dict mapping socket module constants to their names"""
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix)
                 )
families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

#Create a TCP/IP socket
sock = socket.create_connection(('127.0.0.1', 50018))

print >>sys.stderr, 'Family  :', families[sock.family]
print >>sys.stderr, 'Type    :', types[sock.type]
print >>sys.stderr, 'Protocol:', protocols[sock.proto]
print >>sys.stderr

try:
    #Sent data
    message = 'This is the message. It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    #Look for the response
    datas = []
    amount_recived = 0
    amount_expected = len(message)

    while amount_recived < amount_expected:
        data = sock.recv(16)
        datas.append(data)
        amount_recived += len(data)
        
        
finally:
    print >>sys.stderr, 'Message recived.'
    print >>sys.stderr, 'closing socket'
    sock.close()
