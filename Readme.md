# File Transfer Client-Server Application

This project implements a simple file transfer system using a client-server architecture in Python. It allows users to send and receive files between the client and server.

## Files

- `Server.py`: Server-side application
- `Client.py`: Client-side application

## Setup

1. Clone the repository:
    
    ```bash
    git clone https://github.com/aaryanshetty23/file-transfer-application.git
    cd file-transfer-application
    ```
2. Ensure you have Python installed (version 3.6 or higher recommended).

3. No additional dependencies are required.

## Usage

1. Start the server:
    
        ```bash
        python Server.py
        ```
        
        The server will start running on `localhost` at port `8080`.

2. Start the client in a seperate terminal:
    
        ```bash
        python Client.py
        ```
Make sure to update the `SERVER` variable in `Client.py` with the correct IP address of your server.

3. Follow the prompts in the client application to send or receive files.

## Features

- File transfer between client and server
- List available files on both client and server
- Send files from client to server
- Receive files from server to client
- Simple command-line interface



