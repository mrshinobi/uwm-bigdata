import socket
import time


def run_server(port=9999):
    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to the port
    server_socket.bind(("localhost", port))

    # put the socket into listening mode
    server_socket.listen(1)
    print(f"Server listening on port {port}...")

    # accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Received connection from {addr}")

    try:
        count = 0
        while True:
            # send data to the client
            message = f"Message number {count}\n"
            client_socket.send(message.encode("utf-8"))
            count += 1
            time.sleep(1)  # send a message every second
    finally:
        client_socket.close()
        server_socket.close()
        print("Server closed.")


if __name__ == "__main__":
    run_server()
