# This is a small example of socket programming that is able to connect multiple clients to a server using python 3 sockets.
# It can send messages from clients to server, and from server to clients.
# This example also shows how to host the socket server locally or globally across the internet so anyone can connect.
# This uses the python 3 socket and threading module.
import socket
import threading
import pickle                          #inorder to send other data type
PORT = 5050
FORMAT = "UTF-8"
D = "Balance"                               # or any other msg
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname())
#127.0.0.1
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)

def send (msg, client):
	MSG = msg.encode(FORMAT)
	msg_len = len(MSG)
	send_len = str(msg_len).encode(FORMAT)
	send_len +=b' '*(HEADER - len(send_len))
	client.send(send_len)
	client.send(MSG)

def client (conn, addr,clients):
	print(f"{addr} is connected To The Payment Server")
	connected = True
	while connected:
		msg_len = conn.recv(HEADER).decode(FORMAT)
		if msg_len:
			msg_len = int (msg_len)
			msg = conn.recv(msg_len).decode(FORMAT)
			if msg == D:
				connected = False
			print(f"{addr} {msg}")
		for client in clients:
			if client != conn:
				send(msg,client)
	conn.close()

def start():
	server.listen()
	print(f"The Server Is Listening to {SERVER}")
	clients = []
	while True:
		conn,addr = server.accept()
		clients.append(conn)
		thread = threading.Thread(target=client, args=(conn, addr, clients))
		thread.start()
print("Your Payment  Server Is Starting")
start()
