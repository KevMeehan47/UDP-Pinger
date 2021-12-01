import time
import sys
import random
from socket import *

def create_ping():    #Creates a randomly generated 56 byte ping
    ping = []
    for i in range(56):
        num = random.randint(0,255)
        ping.append(format(num, "08b"))
    return ping

def print_ping(ping): #print's ping in hex format
    hex_ping = ""
    for i in range(len(ping)):
        hex_ping += ping[i]
    return hex(int(hex_ping, 2))
        
client_socket = socket(AF_INET, SOCK_DGRAM)     #Creates UDP socket  
client_socket.settimeout(1)                     #Waits 1 second for reply before timing out

host_ip_address = sys.argv[1]
port_number = int(sys.argv[2])
socket_address = (host_ip_address, port_number)

print()
for i in range(5):  #Send 5 pings
    ping = create_ping()
    message = print_ping(ping)
    
    start_time = time.time()    #Starts a time between when message was sent and received
    
    client_socket.sendto(str.encode(message), socket_address)
    
    try:
        data, server = client_socket.recvfrom(1024)
        
        end_time = time.time()
        rtt = end_time - start_time     #Calculates total round trip time for a ping
        
        print("PING", host_ip_address, i, format(rtt * 10**3, ".3f") + " millisecs") 
        print()
    
    except timeout:     #If the transmission times out, the ping is considered lost
        print ("PING", host_ip_address, i, "LOST")
        print()