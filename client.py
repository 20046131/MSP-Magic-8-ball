import socket
from server import server
userinput= True
def client():
    while userinput:
        usersinput = input("Enter your question: ")
        # Create client socket (AF_INET => IP, SOCK_STREAM => TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('127.0.0.1', 5000))
        sock.send(usersinput.encode()) # encodes the userinput and will sent it to the server
        from_server = sock.recv(4096)
        sock.close() # closes the socket to the server
        print(from_server.decode())  # prints the server response to the usersinput

# Run the sever before running the main
if __name__ == '__main__':
    client()