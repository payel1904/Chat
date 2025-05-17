import socket
import threading

clients = []

def handle_client(client_socket, address):
    """Handle messages from a single client"""
    print(f"[NEW CONNECTION] {address} connected.")
    clients.append(client_socket)
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{address}] {message}")
            broadcast(message, client_socket)
        except:
            break
    
    print(f"[DISCONNECTED] {address} left.")
    clients.remove(client_socket)
    client_socket.close()

def broadcast(message, sender_socket):
    """Send message to all clients except sender"""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen()
    print("[SERVER] Listening on port 5555...")
    
    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    start_server()