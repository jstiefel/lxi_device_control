import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.131', 9221))
message1 = '*IDN?\n'
message1 = message1.encode('utf-8')
message2 = 'V1 10'
message2 = message2.encode('utf-8')
s.sendall(message1)
buffer = s.recv(1024)
print(buffer)
s.sendall(message2)