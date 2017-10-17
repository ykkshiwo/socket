import socket   #for sockets
import sys  #for exit
 
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();
 
#print 'Socket Created'

host = '127.0.0.1'
port = 8888

s.connect((host , port))
 
#print 'Socket Connected to ' + host + ' on ip ' + host
'''
try:
    remote_ip = socket.gethostbyname( host )
 
except socket.gaierror:
    #could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()
     
print 'Ip address of ' + host + ' is ' + remote_ip
'''



try :
    #Set the whole string
    while True:
        send_str = raw_input("what message you want to send: ")
        print send_str
        if send_str == "q":
            break
        s.sendall(send_str)
        reply = s.recv(4096)
        print (reply)
except socket.error:
    #Send failed
    print ('Send failed')
    sys.exit()
 

