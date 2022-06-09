# Run it on IDLE python 2
import socket
import Adafruit_DHT

s=socket.socket()

s.bind(("192.168.193.109", 1234))
s.listen(5)
while (True):
    print("Waiting for client connection to establish....")
    c,addr = s.accept()

    humidity,temp = Adafruit_DHT.read_retry(11,4)
    print("Got connection from",addr)
    c.send(str(temp))
    c.close()
