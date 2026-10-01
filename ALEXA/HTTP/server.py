import socket

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Allow reuse of port (IMPORTANT)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 3. Bind to localhost:8000
server_socket.bind(('127.0.0.1', 8000))

# 4. Start listening
server_socket.listen(5)
print(" Server running at http://localhost:8000")

# 5. Keep server alive forever
while True:
    client_socket, addr = server_socket.accept()
    print(f" Connection from {addr}")

    request = client_socket.recv(1024).decode()
    print(" Request:")
    print(request)

    # 6. HTTP response (CORRECT FORMAT)
    body = "HELLO, this is my OWN HTTP SERVER!"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        + body
    )

    client_socket.sendall(response.encode())
    client_socket.close()
