import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print("Повідомлення від сервера: {}".format(message))

        except ConnectionResetError:
            break

    client_socket.close()
    print("З'єднання з сервером закрите.")

def send_message(client_socket):
    while True:
        message = input("Введіть повідомлення: ")
        client_socket.send(message.encode("utf-8"))

        if message.lower() == "закрити":
            break

    client_socket.close()
    print("З'єднання з сервером закрите.")

def start_client():
    host = "127.0.0.1"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print("Підключено до сервера.")

    
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_message, args=(client_socket,))

    receive_thread.start()
    send_thread.start()

start_client()
