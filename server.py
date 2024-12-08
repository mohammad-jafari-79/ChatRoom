import socket
import threading
import sqlite3

class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.client_names = {}
        self.conn = sqlite3.connect('chatroom.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.initialize_database()

    def initialize_database(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sender TEXT,
                message TEXT
            )
        ''')
        self.conn.commit()

    def save_message(self, sender, message):
        self.cursor.execute('INSERT INTO messages (sender, message) VALUES (?, ?)', (sender, message))
        self.conn.commit()

    def fetch_previous_messages(self):
        self.cursor.execute('SELECT sender, message FROM messages')
        return self.cursor.fetchall()

    def start(self):
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f"Server started on {self.host}:{self.port}")

        while True:
            client, address = self.server.accept()
            print(f"Connection established with {address}")

            self.clients.append(client)
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def broadcast(self, message, exclude_client=None):
        for client in self.clients:
            if client != exclude_client:
                try:
                    client.send(message)
                except:
                    pass

    def handle_client(self, client):
        try:
            for _ in range(3):
                client.send(b'Please enter your name: ')
                name = client.recv(1024).decode('utf-8').strip()
                if name:
                    self.client_names[client] = name
                    break

            name = self.client_names.get(client, "Unknown")
            client_ip = client.getpeername()[0]
            join_message = f"[SERVER] {name} ({client_ip}) has joined the chat!\n".encode('utf-8')
            print(join_message.decode('utf-8'))
            self.broadcast(join_message, exclude_client=client)

            client.send(b"[SERVER] Welcome to the chatroom! Here are previous messages:\n")
            for sender, message in self.fetch_previous_messages():
                client.send(f"[{sender}]: {message}\n".encode('utf-8'))

            while True:
                message = client.recv(1024)
                if message:
                    formatted_message = f"[{name}]: {message.decode('utf-8')}\n"
                    self.save_message(name, message.decode('utf-8'))
                    self.broadcast(formatted_message.encode('utf-8'), exclude_client=client)
                else:
                    break

        except:
            pass

        finally:
            self.clients.remove(client)
            leave_message = f"[SERVER] {self.client_names.get(client, 'A user')} has left the chat.\n".encode('utf-8')
            print(leave_message.decode('utf-8'))
            self.broadcast(leave_message)
            client.close()

if __name__ == "__main__":
    server = ChatServer('127.0.0.1', 12345)
    server.start()
