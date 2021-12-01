Part A of ECSE 4670 (Computer Communication Networks) at RPI

Server code:
The server code is available as PingServer.py, which provides a full implementation of
the ping server. You need to compile and run this code. You should study this code
carefully, as it will help you write your ping client. As you study the server code, you will
notice that the server sits in an infinite loop listening for incoming UDP packets. When a
packet comes in, the server simply sends the encapsulated data back to the client.
Note that UDP provides applications with an unreliable transport service, because
messages may get lost in the network due to router queue overflows or other reasons.
However, since packet loss is rare or even non-existent in typical campus networks, this
server code injects artificial loss to simulate the effects of network packet loss. The server
has a parameter LOSS_RATE that determines which percentage of packets should be
lost. The server also has another parameter AVERAGE_DELAY that is used to simulate
transmission delay from sending a packet across the Internet. You should set
AVERAGE_DELAY to a positive value when testing your client and server on the same
machine, or when machines are close by on the network. You can set
AVERAGE_DELAY to 0 to find out the true round-trip times of your packets.

Client code:
In part A of the assignment, your job is to write the ping client code, PingClient.py, so
that the client sends 5 ping requests to the server, separated by approximately one second.
Each ping message consists of 56 bytes of data. As in the actual ping application, these
56 data bytes can be anything, and can be the same for all ping messages. After sending 
each packet, the client starts a timer and waits up to one second to receive a reply. You
will notice in the server code that the ping message (the 56 bytes of data in each UDP
packet) is simply copied into the reply message. Once the reply is received, the client
stops the timer and calculates the round trip time (rtt). If one second goes by without a
reply from the server, then the client assumes that its packet or the server's reply packet
has been lost in the network. For this purpose, you will need to research the API for
DatagramSocket to find out how to set the timeout value on a datagram socket.

Your client should start with the following command:
PingClient.py <host-name> <port-number>
where <host-name> is the name of the computer the server is running on, and <portnumber> is the port number it is listening to. Note that you can run the client and server
either on different machines or on the same machine.

When developing your code, you should run the ping server on your machine, and test
your client by sending packets to localhost (or, 127.0.0.1). After you have fully debugged
your code, you should see how your application communicates between two machines
across the network.

Message Formatting:
The ping messages in this part are to be formatted in a simple way. The client prints on
the screen a one-line message corresponding to each ping request. If the client receives a
response for a ping request, it prints the following line:
  PING <server-ip-address> <sequence-number> <rtt-estimate>
where <server-ip-adress> is the IP address of the server in dotted decimal format,
<sequence-number> starts at 0 and progresses to 4 for each successive ping message sent
by the client, <rtt-estimate> is an estimate of the round-trip time between the client and
the server, calculated as the difference between the time a ping response is received and
the time the request was sent (the timestamp in the response packet). The <rtt-estimate>
is expressed in millisecs, showing up to 3 decimal places (microsec accuracy). Note that
this RTT estimate includes the AVERAGE_DELAY value that is introduced artificially,
and in general may not be a good estimate of the actual RTT.
  
If the client does not receive a response to a ping request within one second of sending it,
it prints the following line:
 PING <server-ip-address> <sequence-number> LOST
