import socket
import random

responses = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.",
             "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
             "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
             "Don't count on it.", "My reply is no.", "My sources say no.", " Outlook not so good.", "Very doubtful."]


QUEUE_SIZE = 5


def server():
    # this will check for a connection to the client
    serv = socket.socket(
               socket.AF_INET,
               socket.SOCK_STREAM)
    serv.bind(('', 5000))
    serv.listen(QUEUE_SIZE)
    print('Sever is running')
    # always listen for connections

    while True:
        conn, addr = serv.accept()# client connected to server
        print(f'Cntn: {addr}')
        from_client= ""
        while True:
            msg = random.choice(responses) # Randomley select a response in the array
            data = conn.recv(4096)
            if not data:
                break
            from_client += data.decode()
            print(f"Response from client {from_client} ") # Will print the client response in the server console
            print(f"severs Response {msg}")# Will print the selected resonance in the server console
            conn.send(msg.encode()) # Encode the response to send back to the client
        conn.close() # Close the connection to the client
        print('client disconnected')

if __name__ == '__main__':
    server()