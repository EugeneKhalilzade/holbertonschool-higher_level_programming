#!/usr/bin/python3
"""Module for basic client-server connection"""


def start_server():
    """Host side"""
    import json
    import socket

    # Specifying the connection way
    HOST = '127.0.0.1'
    PORT = 45678

    # Establishing the connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        # Connection
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:

                # Waiting for user data
                data = conn.recv(1024)

                # Breaking if disconnected
                if not data:
                    break

                # Printing the deserialized data received
                print(json.loads(data))


def send_data():
    import socket
    import json

    # Specifying the connection way
    HOST = "127.0.0.1"
    PORT = 45678

    # Data to be sent
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }

    # Establishing the connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(json.dumps(sample_dict))
