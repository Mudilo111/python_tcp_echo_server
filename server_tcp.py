import socket

addr = ('localhost', 7070)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

server.listen(1)
client_sock, client_addr = server.accept()

while True:
	req = client_sock.recv(1024)
	print('Variant - {0}. From {1}'.format(req.decode('utf-8'), client_addr))
	if req.decode('utf-8') == '1':
		client_sock.send('Please enter 2 numbers\n'.encode('utf-8'))
		data = client_sock.recv(1024)
		nums = data.decode('utf-8').split(' ')
		print(f'Received numbers: {nums}')
		summ = 0
		for i in nums:
			summ += int(i)
		ans = f'Your answer is {summ}\n'
		client_sock.send(ans.encode('utf-8'))
	elif req.decode('utf-8') == '2':
		client_sock.send('Please enter 2 numbers\n'.encode('utf-8'))
		data = client_sock.recv(1024)
		nums = data.decode('utf-8').split(' ')
		print(f'Received numbers: {nums}')
		mul = 1
		for i in nums:
			mul *= int(i)
		ans = f'Your answer is {mul}\n'
		client_sock.send(ans.encode('utf-8'))
	elif req.decode('utf-8') == '3':
		client_sock.send('Please enter 1 number\n'.encode('utf-8'))
		data = client_sock.recv(1024)
		num = int(data.decode('utf-8'))
		print(f'Received number: {num}')
		num += 1
		ans = f'Your answer is {num}\n'
		client_sock.send(ans.encode('utf-8'))
	elif req.decode('utf-8') == 'shutdown':
		break
client_sock.close()
server.close()