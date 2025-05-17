import socket
import threading

def receive_messages(client_socket):
    """Handle incoming messages from server"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("[ERROR] Connection lost!")
            client_socket.close()
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))
    
    # Get username
    username = input("Enter your username: ")
    client.send(username.encode('utf-8'))
    
    # Start receiving messages in a thread
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    # Send messages
    while True:
        message = input()
        if message.lower() == 'exit':
            client.close()
            break
        client.send(message.encode('utf-8'))

if __name__ == "__main__":
    print("[CLIENT] Connecting to server...")
    start_client()