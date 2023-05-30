import socket

def start_server():
    host = "127.0.0.1"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Сервер запущений. Очікування підключення...")

    client_socket, address = server_socket.accept()
    print("Підключився клієнт: {}".format(address))

    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print("Повідомлення від клієнта {}: {}".format(address, message))

            word_count = count_words(message)

            response = "Кількість слів: {}".format(word_count)

            client_socket.send(response.encode("utf-8"))

        except ConnectionResetError:
            break

    client_socket.close()
    print("Клієнт {} відключився.".format(address))

def count_words(text):
    words = text.split()
    return len(words)

start_server()
