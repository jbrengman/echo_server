import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 50000))
s.listen(5)
while (True):
	connection, address = s.accept()
	message = connection.recv(1024)
	if message:
		connection.send(message)
	connection.close()