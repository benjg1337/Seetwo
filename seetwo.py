import socket

def main():
    # Define host and port
    host = '127.0.0.1'  # Change this to your desired IP address
    port = 12345        # Change this to your desired port number

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"[*] Listening on {host}:{port}")
    
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
    
    # Main loop to receive commands and send responses
    while True:
        try:
            # Receive command from client
            command = client_socket.recv(1024).decode()
            if not command:
                break
            
            # Execute command and get output
            output = execute_command(command)
            
            # Send output back to client
            client_socket.send(output.encode())
        except Exception as e:
            print(f"[-] Error: {e}")
            break
    
    # Close the connection
    client_socket.close()
    server_socket.close()

def execute_command(command):
    """
    Executes the given command and returns the output.
    """
    import subprocess
    
    try:
        # Execute the command
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
    except Exception as e:
        output = str(e)
    
    return output

if __name__ == "__main__":
    main()
