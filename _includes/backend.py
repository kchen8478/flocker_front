import socket
import threading
import random

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Arbitrary non-privileged port

# Maintain lists of clients and chat pairs
clients = []
client_pairs = {}

# Server socket setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates rhe socket, manage networks cnnections, "socket.AF_INET" speficies the IP address 127.0.0.1, 
server.bind((HOST, PORT)) #makes it ready to recieve connections on the IP address
server.listen() #makes the server ready to connect clients making it a passive socket intead of an active one

def broadcast(message, sender):
    for client, name in client_pairs[sender]:
        if client != sender:
            client.send(message)

def handle_client(client):
    try:
        # Send initial message
        client.send("Welcome! Waiting for a chat partner...".encode('utf-8'))
       
        # Assign client randomly to a chat pair
        if len(clients) % 2 == 1:  # If odd, connect the last client
            partner = clients[-2]   # Get the previous client
            client_pairs[client] = [client, partner]
            client_pairs[partner] = [client, partner]
            for c in [client, partner]:
                c.send("You are now connected in a private DM.".encode('utf-8'))
        else:
            clients.append(client)

        # Listen for messages
        while True:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)

    except:
        pass
    finally:
        # Remove client from chat
        if client in clients:
            clients.remove(client)
        if client in client_pairs:
            del client_pairs[client]
        client.close()

def receive_clients():
    print("Server started. Waiting for clients to connect...")
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,)).start()

# Start the server to receive clients
receive_clients()