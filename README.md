# Chat
## ✉️ How It Works
🔧 Server (server.py)
Accepts connections from clients.

Creates a new thread for each connected client.

Broadcasts messages from one client to all others.

## 👤 Client (client.py)
Connects to the server.

Sends a username for identification.

Listens for messages in one thread and sends messages from the main thread.

## 📌 Sample Output
### Server:
<pre>
[SERVER] Listening on port 5555...
[NEW CONNECTION] ('127.0.0.1', 50321) connected.
[Alice]: Hello!
[DISCONNECTED] ('127.0.0.1', 50321) left.</pre>
### Client:
<pre>
Enter your username: Alice
[Alice]: Hello!</pre>
## 📤 Future Improvements
GUI using Tkinter or PyQt

Store message history in files or a database

Private messaging between clients

Encryption for secure communication

