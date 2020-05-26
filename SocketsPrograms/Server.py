'''
import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
print (host)
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print ('Got connection from', addr)
   c.send(bytes('Thank you for connecting',"utf-8"))
   c.close()                # Close the connection
'''
#where c is , used to accept a connection. It returns a pair of values (conn, address) ,
# where conn is a new socket object for sending or receiving data and address is the address of the socket present at the other end of the connection


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
# port number can be anything between 0-65535(we usually specify non-previleged ports which are > 1023)
s.listen(5)

while True:
   clt, adr = s.accept()
   print(f"Connection to {adr} established")
   # f string is literal string prefixed with f which
   # contains python expressions inside braces
   clt.send(bytes("Socket Programming in Python", "utf-8 "))  # to send info to clientsocket
