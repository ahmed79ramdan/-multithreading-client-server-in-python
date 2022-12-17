import socket
import threading
import pickle                        #inorder to send other data type
PORT = 5050
FORMAT = "UTF-8"
D = "Balance"                               # or any other msg
HEADER = 64
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

def send (msg):
	MSG = msg.encode(FORMAT)
	msg_len = len(MSG)
	send_len = str(msg_len).encode(FORMAT)
	send_len +=b' '*(HEADER - len(send_len))
	client.send(send_len)
	client.send(MSG)

def read ():
	msg_len = client.recv(HEADER).decode(FORMAT)
	if msg_len:
		msg_len = int (msg_len)
		msg = client.recv(msg_len).decode(FORMAT)
		print(f"{msg}")
x = ''
input(x)
while 1:
    if x!="Balance":
        send(x)
thread = threading.Thread(target=read)
thread.start()
send(D)
