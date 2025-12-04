import socket
import threading
import paramiko
import logging
import sys
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('honeypot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Generate host key
host_key = paramiko.RSAKey.generate(2048)

class SSHServer(paramiko.ServerInterface):
    def __init__(self, ip):
        self.ip = ip

    def check_auth_password(self, username, password):
        logging.info(f"[AUTH] IP={self.ip} USER={username} PASS={password}")
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return "password"

def handle_client(client, addr):
    logging.info(f"[CONNECT] Connection from {addr}")

    try:
        transport = paramiko.Transport(client)
        transport.add_server_key(host_key)
        server = SSHServer(addr[0])

        try:
            transport.start_server(server=server)
            channel = transport.accept(20)
            if channel:
                channel.close()
        except Exception as e:
            logging.info(f"[ERROR] {e}")

        transport.close()
    except Exception as e:
        logging.info(f"[ERROR] Transport failed: {e}")

def start_honeypot():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 22))
    sock.listen(100)

    logging.info("SSH Honeypot Running on port 22...")

    while True:
        client, addr = sock.accept()
        t = threading.Thread(target=handle_client, args=(client, addr))
        t.start()

if __name__ == "__main__":
    start_honeypot()
