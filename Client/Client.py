import socket
import os

HEADER = 64
PORT = 5072
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"
SERVER = "" # Enter the IP address of the server
SIZE=1024
FILENAME=""
FILESIZE=0
ADDR = (SERVER, PORT)
s=""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def receive_file():
    global s
    msg = input(str("Enter the file name to receive: "))
    s=s+msg+"\n"  
    message = msg.encode(FORMAT)  # encode message
    msg_length = len(message)  # get filename length
    send_len = str(msg_length).encode(FORMAT)  # encoding str_len
    send_len += b' ' * (HEADER - len(send_len))  # padding
    client.send(send_len)  # send length
    client.send(message)  # send message
    data = client.recv(2048)  # receive file
    invalid = 1
    while invalid:
        if data.decode(FORMAT) == "Invalid Filename":
            print("This file doesn't exist please enter a valid filename")
            msg = input(str("Enter a valid filename: "))
            message = msg.encode(FORMAT)
            msg_length = len(message)
            send_len = str(msg_length).encode(FORMAT)
            send_len += b' ' * (HEADER - len(send_len))
            client.send(send_len)
            client.send(message)
            data = client.recv(2048)
        else:
            invalid = 0
    filename = input("Enter the name of file: ")
    file = open(filename, 'wb')  # write bytes
    file.write(data)
    file.close()
    print("File received")


def send_file():
    msg = input(str("Enter the file name to send from the client to the server: "))
    j="" 
    j=j+msg # get filename
    FILENAME=msg
    #FILESIZE = os.path.getsize(FILENAME)
    #FILESIZE= os.path.getsize(FILENAME)
    
    FILESIZE = os.path.getsize("Sample_files_cl/"+FILENAME)
    
    message = msg.encode(FORMAT)  # encode message
    msg_length = len(message)  # get filename length
    send_len = str(msg_length).encode(FORMAT)  # encoding str_len
    send_len += b' ' * (HEADER - len(send_len))  # padding
    #client.send(send_len)
    #client.send(message)   # send length
    
    data = f"{FILENAME}_{FILESIZE}"
    client.send(data.encode(FORMAT))
    '''msg = client.recv(SIZE).decode(FORMAT)
    print(f"SERVER: {msg}")'''
 
    # Data transfer 
    
 
    with open("Sample_files_cl/"+FILENAME , "r") as f:
        data = f.read(SIZE)
        print(data)
        client.send(data.encode(FORMAT))
 
s=client.recv(1024).decode()
path = os.path.abspath(__file__)
#path=path[-len(path):-9]
path=path[:-9]


#files = os.listdir(path)
files=os.listdir(path+"/Sample_files_cl")
q=""
for file in files:
    q=q+file+"\n"       
          
    
    



while True:
    
    

    choice = input("Enter 'r' to receive file or 's' to send file or 'q' to quit: ")
    if choice == 'r':
        print("THE FILES IN THE SERVER ARE:\n")
        #print(s+j)
        receive_file()
    elif choice == 's':
        print("THE FILES IN THE CLIENT TO SEND FROM ARE: \n")
        print(q)
        send_file()
    elif choice == 'q':
        message = DISCONNECT.encode(FORMAT)  # encode message
        msg_length = len(message)  # get filename length
        send_len = str(msg_length).encode(FORMAT)  # encoding str_len
        #send_len += b' ' * (HEADER - len(send_len))  # padding
        client.send(send_len)  # send length
        client.send(message)  # send message
        break
    else:
        print("Invalid choice. Please try again.")

client.close()
