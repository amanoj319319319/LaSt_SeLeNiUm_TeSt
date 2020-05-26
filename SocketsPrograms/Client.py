'''
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print (host)
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024).decode())
s.close()                     # Close the socket when done
'''
#https://www.edureka.co/blog/socket-programming-python/ (please refer this url)

import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2346))
msg=s.recv(1024)
print(msg.decode("utf-8"))