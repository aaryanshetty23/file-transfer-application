import socket
import threading
import os

HEADER = 64
PORT = 5072
SIZE=1024
FORMAT = 'utf-8'
DISCONNECT = "!DISCONNECT"
SERVER = "0.0.0.0"
ADDR = (SERVER, PORT)
FINAL=""
print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        global msg_length 

        try:
            msg_length= conn.recv(HEADER).decode(FORMAT)
        except:
            pass
        else:

        
            if msg_length:
                print("m1",msg_length)
                msg_length = msg_length.split("_")[0]
                msg_length = int(msg_length.strip())
                #print(msg_length)
                try:
                    msg = conn.recv(int(msg_length)).decode(FORMAT)
                except:
                    send(conn)
                else:
                    print("m2",msg)

                    if msg == "!DISCONNECT":
                        connected = False
                        print(f"[{addr}] {msg}")
                
                    elif os.path.isfile("Sample_files_sr/"+msg):
                        try:
                            print("File exists")
                            with open("Sample_files_sr/"+msg, 'rb') as file:
                                file_data = file.read()
                                conn.send(file_data)
                                print("File sent")
                        except IOError:
                            conn.send("Invalid Filename".encode(FORMAT))
                    else:
                        conn.send("Invalid Filename".encode(FORMAT))
    
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        path = os.path.abspath(__file__)
        path=path[-len(path):-9]
        print(path)



        # how to add os.listdir(path/"Server/Sample_files_sr") to the FINAL variable
        files = os.listdir(path+"/Sample_files_sr")
        
        si=""
        for file in files:
            print(file)
            si=si+file+"\n"
        FINAL = f"{si}"
        conn.send(FINAL.encode())
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

def send(conn):
    
    data = conn.recv(SIZE).decode(FORMAT)

    item = data.split("_")
    hello = item[0]
    data=msg_length
    item = data.split("_")
    FILENAME=item[0]
    print(FILENAME)
    FILESIZE = int(item[1])
 
    print("[+] Filename and filesize received from the client.")
    #conn.send("Filename and filesize received".encode(FORMAT))
    with open("Sample_files_sr/"+FILENAME , "w") as f:
        
        #data = conn.recv(SIZE).decode(FORMAT)
        #print("FILE CONTENT",data)
        f.write(hello)
        print("Done writing")
        f.close()
        
 
            
    
    #conn.close()
    #server.close()

print("Server is now listening...")
start()
