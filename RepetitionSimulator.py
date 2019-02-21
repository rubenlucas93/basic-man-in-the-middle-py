import socket, time
 
UDP_IP = "127.0.0.1"
UDP_PORT = 3300
UDP_PORT_ORIGIN=23002
UDP_PORT_DESTINATION=3800
previousTimestamp = 0

def replaceTimestamp(data):
    b = data[0:8] + bytearray(data[8]+1) + data[9:]
    return b
	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT))


while True:
    #RECEIVE FROM ORIGIN
    rail9kData, addr = sock.recvfrom(256) # buffer size is 1024 bytes
    print ("received message:", int.from_bytes(rail9kData[1:5], byteorder='big', signed=False))
    #SEND TO DESTINATION
    sock.sendto(rail9kData, (UDP_IP, UDP_PORT_DESTINATION))
	
    #RECEIVE FROM DESTINATION
    dataInterlock, addr = sock.recvfrom(256)
    print ("received message:", dataInterlock)
	
	#MODIFY RECEIVED MESSAGE
    dataModified = replaceTimestamp(dataInterlock)
    print ("modified message:", dataModified)

	#SEND TWO MESSAGE TO ORIGIN
    sock.sendto(dataInterlock, (UDP_IP, UDP_PORT_ORIGIN))
    sock.sendto(dataModified, (UDP_IP, UDP_PORT_ORIGIN))



	
	
        