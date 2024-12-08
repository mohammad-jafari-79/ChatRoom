import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client.connect((self.host, self.port))
        print("Connected to the server.")

        thread = threading.Thread(target=self.receive_messages)
        thread.start()

        while True:
            message = input()
            if message:
                self.client.send(message.encode('utf-8'))

    def receive_messages(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                if message:
                    print(message)
            except:
                print("Disconnected from the server.")
                self.client.close()
                break

if __name__ == "__main__":
    client = ChatClient('127.0.0.1cc', 12345)
    client.start()
