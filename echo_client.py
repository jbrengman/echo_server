import socket
import sys

def main():
	if (len(sys.argv) > 1 and type(sys.argv[1]) == str):
		message = sys.argv[1]
	else:
		message = raw_input('Enter a message to send and recieve: ')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 50000))
	s.sendall(message)
	recieved_message = s.recv(1024)
	s.close()
	print(recieved_message)

if __name__ == '__main__':
	main()