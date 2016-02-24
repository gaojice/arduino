import socket
from flask import Flask,request
                                                  
app=Flask(__name__)
arduino_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
arduino_sock.connect(('192.168.0.14',8899))

@app.route('/')
def index():
        arduino_sock.sendall(request.args.get('command')+'\r\n')
	
        print 'send ok.'
	d=arduino_sock.recv(256)
	return d

if __name__=='__main__':
	app.run(host='0.0.0.0',port=8899,debug=True)
