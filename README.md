# Chat Server and Client (Python)

This project is part of my exercise in the Python programming course. It implements a simple chatroom application using Python's `socket` and `threading` modules, with SQLite for storing chat messages. It consists of two main files: `server.py` (the server) and `client.py` (the client).

## Overview
---
The chat server listens for incoming client connections, handles multiple clients concurrently, and stores chat messages in a SQLite database. The client connects to the server, allows users to send messages, and displays incoming messages from other users.

### Features

- Real-time chat communication between clients.
- Message history stored in an SQLite database.
- Broadcasting of messages to all connected clients (except the sender).
- Basic error handling for client disconnections.

## Files
---
### `server.py` - Chat Server

- Initializes a socket server, listens for incoming connections on a specified host and port.
- Manages a list of connected clients and their names.
- Stores chat messages in an SQLite database.
- Broadcasts messages to all clients and handles user join/leave notifications.
- Prompts each client to enter their name when they first connect.
- Displays previous messages stored in the database upon a client's connection.

### `client.py` - Chat Client

- Connects to the chat server and allows users to send messages.
- Displays messages from other clients in real-time.
- A separate thread listens for incoming messages from the server.
- Handles graceful disconnection if the server is unavailable.

## How to Use
---
### 1. Run the Server

To start the chat server, execute the `server.py` script. The server will listen for incoming client connections on `127.0.0.1:12345` by default.

```bash
python server.py
```

### 2. Run the Client(s)
To start a client, execute the client.py script. Each client will connect to the server and be able to send and receive messages.

```bash
python client.py
```

You can run multiple instances of the client.py script to simulate multiple clients.

### 3. Chatting
Once a client connects, it will be prompted to enter a username.
The client can then send messages, and all connected clients will receive the broadcasted messages.
The server stores each message in the database, which is fetched and displayed for new clients upon connection.

#### Requirements
- Python 3.x
- No external dependencies are required, other than the built-in socket, threading, and sqlite3 modules.
- About the Project
- This project is an exercise for my Python programming course, where I learned key concepts like socket programming, threading, and database management with SQLite.

## Connect with My Teacher
---
You can reach out to my teacher via Instagram for more information or help.

<a href="https://www.instagram.com/hosein_rad_art">
  <img width="40px" height="40px" src="icons/instagram.svg"/ alt="Instagram Icon">
<br><br>

<a href="https://iconscout.com/icons/instagram" target="_blank">Instagram Icon</a> by <a href="https://iconscout.com/contributors/juraj-sedlak">Juraj Sedlák</a> on <a href="https://iconscout.com">IconScout</a><br>
