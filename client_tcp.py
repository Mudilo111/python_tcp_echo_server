import socket

addr = ('localhost', 7070)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(addr)

print('This program can count sum/multiplicaton for two numbers or increment one number!\n')
while True:
	print('1. Count sum of two numbers\n'
		  '2. Count multiplicaton of two numbers\n' 
		  '3. Increment one number\n'
		  'To exit print: "exit"\n')

	var = input('Choose variant: ')
	if var == 'exit':
		client.send('shutdown'.encode('utf-8'))
		break

	client.send(var.encode('utf-8'))
	resp = client.recv(1024)
	print(resp.decode('utf-8'))
	data = input()
	client.send(data.encode('utf-8'))
	print(client.recv(1024).decode('utf-8'))
client.close()