import socket
import sys

def main(argv):
	# pass
	if (argv[0] and type(argv[0]) == str):
		message = argv[0]
	else:
		message = raw_input('Enter a message to send and recieve: ')

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('127.0.0.1', 50000))
	s.sendall(message)
	received_message = s.recv(1024)
	s.close()
	#print(received_message)
	return received_message

if __name__ == '__main__':
	main(sys.argv[1:])