import socket
import sys
import time

def udp_echo_client(server_host, server_port, num_msgs, num_bytes):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    message = '\x00' * num_bytes  # Create a message with null bytes of the specified size
    message_size = sys.getsizeof(message)  # Get the size of the message

    for seq_num in range(1, num_msgs + 1):
        time_before = time.time()  # Record the time before sending the message
        client_socket.sendto(message.encode('utf-8'), (server_host, server_port))
        
        data, server_address = client_socket.recvfrom(10240)  # Receive echoed data
        time_after = time.time()  # Record the time after receiving the response
        
        rtt = time_after - time_before  # Calculate round trip time (RTT)
        
        print(f"Message sequence {seq_num} with size {message_size} bytes received from {server_address} with RTT {rtt:.4f} s")

if __name__ == "__main__":
    server_host = ""  # Match the server IP
    server_port = 42303  # Match the port
    num_msgs = 100  # Number of messages to send
    
    # Experiment 1: Send 100 messages of 1000 Bytes
    num_bytes = 1000  # Size of each message in bytes
    udp_echo_client(server_host, server_port, num_msgs, num_bytes)
    
    # Experiment 2: Send 100 messages of 5000 Bytes
    num_bytes = 5000
    udp_echo_client(server_host, server_port, num_msgs, num_bytes)
    
    # Experiment 3: Send 100 messages of 10000 Bytes
    num_bytes = 10000
    udp_echo_client(server_host, server_port, num_msgs, num_bytes)
