# Run it on terminal
import socket
s=socket.socket()
s.connect(("192.168.193.109",1234))
print("The temperature is ::",s.recv(1234))
s.close()
