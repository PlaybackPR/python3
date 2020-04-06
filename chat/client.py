import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.17.9.193', 8111))
client.send("I am CLIENT<br>")
from_server = client.recv(4096)
client.close()
print (from_server)