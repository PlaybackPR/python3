import socket

SERVER_ADDRESS = ('localhost', 8125)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)
clients = []
members = {}
print("Server is running")