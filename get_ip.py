import socket

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Connect to an external server (Google's DNS)
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip
