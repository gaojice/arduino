import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.0.14',8899))
s.send('on')
buffer=[]
while True:
	d=s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data=''.join(buffer)	
s.close
print data 