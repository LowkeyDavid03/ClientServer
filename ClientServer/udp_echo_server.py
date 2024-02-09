import socket

def udp_echo_server(host, port):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind the server socket to the specified host and port
    server_socket.bind((host, port))
    print(f"UDP Echo Server is listening on {host}:{port}")
    
    while True:
        data, client_address = server_socket.recvfrom(10240)  # Receive data from the client
        print(f"Received message from {client_address}: {data.decode('utf-8')}")
        
        # Echo the received data back to the client
        server_socket.sendto(data, client_address)
        print(f"Echoed message to {client_address}: {data.decode('utf-8')}")

if __name__ == "__main__":
    host = ""  # available ip network interfaces
    port = 42303  # port
    udp_echo_server(host, port)