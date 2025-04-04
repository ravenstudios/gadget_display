import socket

def get_battery():
    try:
        host = "127.0.0.1"
        port = 8423
        message = "get battery"

        # Create a socket connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(message.encode())  # Send the message
            response = s.recv(1024).decode()  # Receive the response

        return response[9:-1]
    except Exception as e:
        return f"Error: {e}"
