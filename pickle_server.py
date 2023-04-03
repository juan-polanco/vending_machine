from Coffee import *
import pickle
import socket
HOST = '127.0.0.1'
PORT = 65432
# step 1 Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2  Bind host and a port with a specific socket
server_socket.bind((HOST, PORT))

# step 3 Listen for a connection from the client
server_socket.listen(1)
print('Loading')

# step 4 Accept requests from a client socket, keeps waiting for incoming connections
socket_client, (host, port) = server_socket.accept()
print(f'Received connection from {host} ({port})\n')
print(f'Connection Established., Connected from: {host}')

# step 5 Unpicking
received_data = socket_client.recv(1024)
received_object = pickle.loads(received_data)
print(f': The client said: {received_object} ')
 if (received_object[:3]=='your object'):
 	your.function



# step 6 Close the connection
socket_client.close()
